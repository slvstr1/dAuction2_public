/*
 * Contains the controller element for auction interface for premia projects, connected via AJAX to backend
 * other elements are present in static/js/auct_elemets and contains advanced logic, just displays what is
 * also fires different MODALS during the game
 */
// used functions
/// define sorting function
var sort_by = function (field, reverse, primer) {
    var key = primer ?
        function (x) {
            return primer(x[field])
        } :
        function (x) {
            return x[field]
        };
    reverse = !reverse ? 1 : -1;
    return function (a, b) {
        return a = key(a), b = key(b), reverse * ((a > b) - (b > a));
    }
};


// define used globals and connect to ReactBootstrap
window.checker1 = true;
window.checker2 = true;
var Navbar = ReactBootstrap.Navbar,
    Nav = ReactBootstrap.Nav,
    NavItem = ReactBootstrap.NavItem,
    NavDropdown = ReactBootstrap.NavDropdown,
    MenuItem = ReactBootstrap.MenuItem,
    Modal = ReactBootstrap.Modal,
    Button = ReactBootstrap.Button;

/// Main container for all objects
var Auction_interface = React.createClass({
    // 1. Define used functions
    // get Auction from API
    getInitialState: function () {
        return {
            phase: [],
            pr_no_UD: true,
            period: [],
            auction: [],
            player: [],
            my_offers_standing: [],
            my_offers_cleared: [],
            player_stats: [],
            history: [],
            vouchers: [],
            active_offers: [],
            timer: [],
            my_position: [],
            all_offers: [],
            auction_id: [],
            user_id: [],
            player_id: [],
            group_id: [],
            data: 0,
            refresh_time: 2000,
            pagerefresh_now: false,
            refreshed: 1,
            last_call: 1,
            in_sync: "N/A",
            penalty: {},
            educational: false,
            only_spot : false
        };
    },
    // fetch id data from django rendered html after page loads
    fetchIdData: function () {
        var auction_id = parseInt($('#auction_id').text());
        var user_id = parseInt($('#user_id').text());
        var player_id = parseInt($('#player_id ').text());
        var group_id = parseInt($('#group_id').text());
        window.group_id = group_id;
        var refresh_time = parseInt($('#refresh_time').text());
        this.setState({
            auction_id: auction_id,
            user_id: user_id,
            player_id: player_id,
            group_id: group_id,
            refresh_time: refresh_time
        });
    },
    fetchHistoryData: function () {
        // feches history data and saves then to state, called at render and every period change
        $.ajax({
            type: "POST",
            url: "/api/history_data",
            data: {
                'auction_id': this.state.auction_id,
                'user_id': this.state.user_id,
                'player_id': this.state.player_id,
                'group_id': this.state.group_id
            },
            success: function (data, status) {
                var history = data.history;
                this.setState({
                    history: history,
                });
            }.bind(this)
        })
    },
    fetchAuctionData: function () {
        $.ajax({
            type: "POST",
            url: "/api/auction_data",
            data: {
                'auction_id': this.state.auction_id,
                'user_id': this.state.user_id,
                'player_id': this.state.player_id,
                'group_id': this.state.group_id
            },
            success: function (data, status) {
                if (data.pagerefresh_now == true) {
                    $.post("/api/refresh/", {"refreshed": "1", 'user_id': this.state.user_id});
                    location.reload();
                }
                // refresh time
                var d = new Date();
                var refreshed = d.getTime();
                // penalty data
                if (data.penalty_list_data !== null) {
                    var penalty_filtered = $.grep(data.penalty_list_data, function (n, i) {
                        return n.player_stats_id == data.player_stats[0].id;

                    });
                    var penalty_data = penalty_filtered.sort(sort_by("id", false, parseInt));
                    var penalty_copy = JSON.parse(JSON.stringify(penalty_data));
                    // add number to it
                    for (var key in penalty_copy) {
                        if (penalty_copy.hasOwnProperty(key)) {
                            penalty_copy[key].n = parseInt(key) + 1;
                            penalty_copy[key].id_web = "pen" + String(parseInt(key) + 1)

                        }
                    }

                } else {
                    var penalty_copy = null
                }
                ;

                // phase
                var phase = data.phase;
                // period
                var period = data.period;
                // auction
                var auction = data.auction;
                // player(user) object
                var player = data.player;
                // split offers to my offers and general offers
                var active_offers_copy = JSON.parse(JSON.stringify(data.all_offers_ser));
                var all_offers = data.all_offers_ser;
                var my_offers = $.grep(data.all_offers_ser, function (n, i) {
                    return n.player_id == data.player.id;
                });
                var my_offers_standing = $.grep(my_offers, function (n, i) {
                    return n.cleared == false;
                });
                var my_offers_cleared = $.grep(my_offers, function (n, i) {
                    return n.cleared == true;
                });
                // my vouchers
                /// if player is RE, vouchers are not sent, have to be generated
                if (data.player.role == 1) {
                    var vouchers = [];

                } else {
                    var vouchers = data.vouchers;
                }
                // player stats for current period, active offers
                var player_stats = data.player_stats[0];

                var active_offers = $.grep(active_offers_copy, function (n, i) {
                    return n.cleared == false;
                });
                // timer
                var timer = data.timer;
                // calculate my position
                var my_position = player_stats.vouchers_used - player_stats.vouchers_negative;
                this.setState({
                    pr_no_UD: auction.require_units_demanded_on_PR,
                    pagerefresh_now: data.pagerefresh_now,
                    educational: data.auction.educational,
                    only_spot: data.auction.only_spot,
                    phase: phase,
                    period: period,
                    auction: auction,
                    player: player,
                    my_offers_standing: my_offers_standing,
                    my_offers_cleared: my_offers_cleared,
                    vouchers: vouchers,
                    player_stats: player_stats,
                    active_offers: active_offers,
                    timer: timer,
                    data: 1,
                    my_position: my_position,
                    all_offers: all_offers,
                    refresh_time: auction.time_refresh_data,
                    refreshed: refreshed,
                    penalty: penalty_copy
                });
            }.bind(this)
        });
    },
    // dynamic refreshing of auction fetch time
    // this function is triggered only when refresh_time from API call is changed
    componentDidUpdate: function (prevProps, prevState) {
        if (prevState.refresh_time != this.state.refresh_time) {
            // clear all used intervals
            clearInterval(window.refreshIntervalId);
            clearInterval(window.refreshInterval);
            clearInterval(window.refreshIntervalSlow);
            window.refreshInterval = setInterval(function () {
                this.fetchAuctionData();
                this.setState({
                    last_call: new Date().getTime()
                });
                //console.log("changed timer")
            }.bind(this), this.state.refresh_time);
            //console.log("changed")
        }
    },

    // fetch data on reload immediately, then refresh data in 2 sec interval
    // 2. Firing order of all the functions
    componentWillMount: function () {
        this.fetchIdData();
        // give React time to first load ids from the page and then start POST AJAX calls
        setTimeout(function () {
            this.setState({
                last_call: new Date().getTime()
            });
            this.fetchAuctionData();
            // player ready
            $.get("/api/player_ready/", function (data) {
            });
            window.refreshIntervalId = setInterval(function () {
                this.setState({
                    last_call: new Date().getTime()
                });
                this.fetchAuctionData()
            }.bind(this), this.state.refresh_time);
            // check sync and set refresh interval dynamically
            setTimeout(function () {
                setInterval(function () {
                    // check if in sync
                    var d = new Date().getTime();
                    var last_update = this.state.refreshed;
                    var last_call = this.state.last_call;
                    var answer_time = last_update - last_call;
                    // positive if ok, there is a response
                    // can be also a little negative, possible mismatch between updates
                    //console.log(answer_time);
                    if (answer_time > 0 || answer_time + Math.max(this.state.refresh_time, 1000) > 0) {
                        //console.log("ok");
                        this.setState({
                            in_sync: "Connected"
                        });
                        // clear slow
                        clearInterval(window.refreshIntervalSlow);
                        // if slow was started and refreshed was not started, restart
                        if (window.checker2 == true && window.checker1 == false) {
                            window.refreshInterval = setInterval(function () {
                                this.fetchAuctionData();
                                //console.log("new, restart");
                                this.setState({
                                    last_call: new Date().getTime()
                                });
                            }.bind(this), this.state.refresh_time)
                            // start boolean
                            window.checker2 = false;
                        }
                        // allow slow to be restarted
                        window.checker1 = true;
                        // is more then negative, absolute or just a little dc
                    } else if (answer_time < 0) {
                        if (answer_time + 10000 < 0) {
                            //console.log("total dc");
                            this.setState({
                                in_sync: "Disconnected, slow calls mode"
                            });
                            // stop all other intervals
                            clearInterval(window.refreshIntervalId);
                            clearInterval(window.refreshInterval);
                            // reset start of fast interval
                            window.checker2 = true;
                            // is slow one was not started, start it
                            if (window.checker1 == true) {
                                window.refreshIntervalSlow = setInterval(function () {
                                    this.fetchAuctionData();
                                    //console.log("slow")
                                    this.setState({
                                        last_call: new Date().getTime()
                                    });
                                }.bind(this), 10000);
                                // toogle start bolean
                                window.checker1 = false;
                            }
                        } else {
                            //console.log("disconnect)");
                            this.setState({
                                in_sync: "Disconnected"
                            });
                            // clear slow interval if running
                            clearInterval(window.refreshIntervalSlow);
                            // reset booleans for restart and slow
                            window.checker1 = true;
                            window.checker2 = true;
                        }

                    }
                }.bind(this), 1000);
            }.bind(this), 1500);
            setTimeout(function () {
                this.fetchHistoryData();
            }.bind(this), 500);
        }.bind(this), 500);
    },
    // rethink updates to use dynamic values
    componentWillReceiveProps: function (nextProps) {
        // fire AJAX if period changes
        // if (this.props.period.idd != nextProps.period.idd) {
        //     this.fetchHistoryDataC();
        // } else {
        //     //console.log("Nope!");
        // }
        // if (this.props.phase.waiting_page == true | nextProps.phase.waiting_page == true) {
        //     this.setState({
        //         show_distrib: false,
        //         show_history: false,
        //         show_modal: false})
        // }
        console.log(this.props.refresh_time)
        console.log(nextProps.refresh_time)

    },
    // define function for hiding the modal
         hide_modal: function (){
            //collapse
            if ($('.pemodal-content').hasClass('collapse')){
                $('.pemodal-content').removeClass('collapse');
                $('#results_button').text('CLICK to view Trading Screen');
            } else {
                $('.pemodal-content').addClass('collapse');
                $('#results_button').text('CLICK to return to Results Summary');
            }
            // change text

            },
    render: function () {
        // if data are loaded
        if (this.state.data == 1) {
            // DISPLAYING THE QUESTION PAGE
            if (this.state.phase.question_page == true) {
                var Diver =
                    <div className="static-modal">
                        <Modal show="true" bsClass="modal" enforceFocus="true">
                            <Modal.Dialog bsClass="modal-dialog">
                                <Modal.Header bsClass="modal">
                                    <Modal.Title bsClass="modal">
                                        <div style={{textAlign: "right"}}>
                                            <div style={{display: "inlineBlock"}}><h2>Time remaining to answer:
                                                <b> {this.state.timer.seconds_left}</b></h2></div>
                                        </div>

                                        <center><h2>The coming round is about to start in a short moment.<br/><br/>
                                            In the meantime, please answer the following questions.
                                        </h2>

                                            <br/>
                                            <h2> As we informed you before, every round the MARKET UNITS DEMANDED is drawn at
                                                random as a number between {this.state.auction.uniform_min} and {this.state.auction.uniform_max} with each number having an equal
                                                probability to be drawn.</h2>
                                        </center>
                                    </Modal.Title>
                                </Modal.Header >
                                <Modal.Body bsClass="modal">
                                    <Questions_endround    educational = {this.state.educational} timer={this.state.timer}/>
                                </Modal.Body>
                            </Modal.Dialog>
                        </Modal>
                    </div>;
            } else {
                var Diver =
                    <div className="static-modal">
                    </div>;
            }

            // DISPLAY VOUCHER TABLES AND INFOBOX BASED ON PHASE
                 // Stage indicator based on educational settings
                if (this.state.educational == false) {
                    var stage_indicator1 = <span>Stage 1</span>
                    var stage_indicator2 = <span>Stage 2</span>
                     var name_framing = <span>experiment</span>
                } else {
                   var stage_indicator1 = <span>the Forward Market</span>
                   var stage_indicator2 = <span>the Spot Market</span>
                     var name_framing = <span>Business Game</span>
                }
            var units_remaining = this.state.my_position - this.state.player_stats.player_demand;
            var a_units_remaining = Math.abs(units_remaining);
            // retailer
            if (this.state.player_stats.role == 1) {
                // position indicator
                if (units_remaining < 0) {
                    var position = <p> You currently have {this.state.my_position} unit(s) and you need to
                        obtain {a_units_remaining} more to not face any penalty.</p>;
                } else if (units_remaining > 0) {
                    var position = <p> You currently have {this.state.my_position} units and you can sell {a_units_remaining} units. </p>;
                } else if (units_remaining == 0) {
                    var position = <p> You currently have {this.state.my_position} units, exactly the amount
                        required. </p>;
                }
                // what to display when
                if (this.state.phase.idd == 1) {
                    var Infobox =
                        <div>
                            <p>Earnings per Unit is: </p>
                            <ul>
                                <li> {this.state.auction.retail_price} for the number of UNITS DEMANDED</li>
                                <li> 0 for all following units</li>
                            </ul>
                            <p>Obtaining less than the number of UNITS DEMANDED will result in a penalty.</p>
                            <strong>The number of UNITS DEMANDED will be announced in {stage_indicator2} -
                                hence the question marks ("?") now in  {stage_indicator1} </strong></div>

                    var VoucherT = <Voucher_Table
                        role={this.state.player_stats.role}
                        vouchers={this.state.vouchers} auction={this.state.auction}
                        player_stats={this.state.player_stats}
                        educational={this.state.educational}/>;
                } else {
                    var Infobox = <div>
                        <p>Earnings per Unit is: </p>
                        <ul>
                            <li> {this.state.auction.retail_price} for the first {this.state.player_stats.player_demand} units</li>
                            <li> 0 for all following units</li>
                        </ul>
                        <p>Obtaining less than {this.state.player_stats.player_demand} units will result in a
                            penalty. <b>Buy in total at least this number of units.</b></p>
                        {position}
                    </div>
                    var VoucherT = <Voucher_Table2R
                        role={this.state.player_stats.role}
                        vouchers={this.state.vouchers} auction={this.state.auction}
                        player_stats={this.state.player_stats}
                        educational = {this.state.educational}
                        only_spot = {this.state.only_spot}/>;
                }
            }
            // producer
            if (this.state.player_stats.role == 0) {
                // position indicators
                if (units_remaining < 0) {
                    var position = <p> You currently sold {this.state.my_position} unit(s) and you need to
                        sell {a_units_remaining} more to not face any penalty. </p>;
                } else if (units_remaining > 0) {
                    var position = <p> You currently sold {this.state.my_position} units and you can buy back
                         {a_units_remaining} units. </p>;
                } else if (units_remaining == 0) {
                    var position = <p> You currently sold {this.state.my_position} units, exactly the amount
                        required. </p>;
                }
                // what do display and when
                if (this.state.phase.idd == 1) {
                    // if no UD is required, change the text, vouchers remain the same
                     if (this.state.pr_no_UD == false) {
                        var Infobox =
                             <div>
                               <p> </p>
                             </div>
                     } else {
                            var Infobox =
                             <div>
                                 <p> There will be a minimal required number of UNITS DEMANDED, that you have to sell,
                                     announced in {stage_indicator2}. </p>
                                 <p><b>Selling less than the number of UNITS DEMANDED will result in a penalty.</b>
                                 </p>
                             </div>
                     }
                    var VoucherT = <Voucher_Table
                        role={this.state.player_stats.role}
                        vouchers={this.state.vouchers} auction={this.state.auction}
                        player_stats={this.state.player_stats}
                        educational={this.state.educational}/>;
                } else {
                    // if PR has no quota, change the textbox text and voucher table to be same as in ST1
                      if (this.state.pr_no_UD == false) {
                            var Infobox = <div>
                              <p>UNITS DEMANDED was announced to the retailers.</p>
                            </div>
                          var VoucherT = <Voucher_Table
                        role={this.state.player_stats.role}
                        vouchers={this.state.vouchers} auction={this.state.auction}
                        player_stats={this.state.player_stats}
                        educational={this.state.educational}/>;

                      } else {
                          var Infobox = <div>
                              <p>Minimal number of Units demanded for this round is: </p>
                              <ul>
                                  <li> {this.state.player_stats.player_demand} </li>
                              </ul>
                              <p>Selling less than {this.state.player_stats.player_demand} units will result in a
                                  penalty. <b>Sell at least this number of units.</b></p>
                              {position}
                          </div>
                          var VoucherT = <Voucher_Table2R
                              role={this.state.player_stats.role}
                              vouchers={this.state.vouchers} auction={this.state.auction}
                              player_stats={this.state.player_stats}
                              educational={this.state.educational}
                              only_spot={this.state.only_spot}/>;
                      }
                }


            }

            // WAITING PAGES DISPLAY AND TRANSITION DISPLAYS
            // DEFINED AND A MODAL "DIVER" AND DISPLAYED IN THE INTERFACE BY TRIGGERS
            // button for closing up the results modal
            /// hide modal function
            if  (this.state.phase.waiting_page == true && this.state.phase.idd == 2){
                var Results_button = <div
                       style={{
                            position: "absolute",
                            top: "10.5%",
                            right: 0,
                            bottom: "98.5%",
                            left: "70%",
                            background: "whitesmoke",
                           zIndex: 4000

               }}>     <button id="results_button" className="btn btn-primary btn-lg" onClick = {this.hide_modal}><b>CLICK to view Trading Screen</b></button>      </div>
            } else {
                var Results_button = <div></div>;
            };

            // modal before auction is started
            if (this.state.auction.app == 4 && this.state.auction.auction_started == false) {
                if (this.state.player.role == 0) {
                    var c_role = "Producer";
                } else {
                    var c_role = "Retailer";
                }
                var Diver =
                    <div className="static-modal">
                        <Modal show="true" bsClass="pmodal" enforceFocus="true">
                            <Modal.Dialog bsClass="modal-dialog">
                                <Modal.Header bsClass="pmodal">
                                    <Modal.Title bsClass="pmodal"> Please wait for auction to start....</Modal.Title>
                                </Modal.Header >
                                <Modal.Body bsClass="pmodal">
                                    <p> </p>
                                    <p> After a short moment, auction will start. </p>
                                    <p> <h3> You have the role of <b>{c_role}</b> in the {name_framing}.</h3> </p>
                                </Modal.Body>
                            </Modal.Dialog>
                        </Modal>
                    </div>
            }
            // MODALS INSIDE THE AUCTION
            if (this.state.phase.waiting_page == true) {
                var penalty_rounded = Math.round(this.state.player_stats.penalty);
                // TRANSITION BETWEEN STAGES
                if (this.state.phase.idd == 1) {
                    // state transition for RE
                    if (this.state.player.role == 1) {
                        var units_remaining = this.state.my_position - this.state.player_stats.player_demand;
                        var a_units_remaining = Math.abs(units_remaining);
                        if (units_remaining < 0) {
                            var position = <p> You currently have {this.state.my_position} units and you need to
                                obtain {a_units_remaining} more to not face any penalty. </p>;
                        } else if (units_remaining > 0) {
                            var position = <p> You currently have {this.state.my_position} units and you have
                                excess {a_units_remaining} units. </p>;
                        } else if (units_remaining == 0) {
                            var position = <p> You currently have {this.state.my_position} units, exactly the amount
                                required. </p>;
                        }

                        var Warning = <div>
                            <p>UNITS DEMANDED has been set to {this.state.player_stats.player_demand}.</p>
                            <div id='testingPlot'></div>
                            <p>{position}</p>
                        </div>
                    } else {
                        var Waring = <div></div>
                    }
                    // state transition for PR
                    if (this.state.player.role == 0) {
                        if (this.state.pr_no_UD == false) {
                              var Warning = <div>
                           <p></p>
                            </div>
                        } else {
                            var units_remaining = this.state.my_position - this.state.player_stats.player_demand;
                            var a_units_remaining = Math.abs(units_remaining);
                            if (units_remaining < 0) {
                                var position = <p> You currently have sold {this.state.my_position} units and you need
                                    to
                                    sell {a_units_remaining} more to not face any penalty. </p>;
                            } else if (units_remaining > 0) {
                                var position = <p> You currently have sold {this.state.my_position} units and you
                                    are {a_units_remaining} units over minimal quota. </p>;
                            } else if (units_remaining == 0) {
                                var position = <p> You currently have {this.state.my_position} units, exactly the
                                    minimal
                                    amount
                                    required. </p>;
                            }

                            var Warning = <div>
                                <p>UNITS DEMANDED has been set to {this.state.player_stats.player_demand}</p>
                                <div id='testingPlot'></div>
                                <p>{position}</p>
                            </div>
                        }
                    }
                    // base of the modal
                    var Diver =
                        <div className="static-modal">
                            <Modal show="true" bsClass="pmodal" enforceFocus="true">
                                <Modal.Dialog bsClass="pmodal-dialog">
                                    <Modal.Header bsClass="pmodal">
                                        <Modal.Title bsClass="pmodal"><b> {stage_indicator1} has ended.</b></Modal.Title>
                                    </Modal.Header >
                                    <Modal.Body bsClass="pmodal">
                                        <p>Please take a moment to reflect on your choices and the outcomes of the
                                            market.</p>
                                        {Warning}
                                        <p>After a short moment the market continues with {stage_indicator2}.</p>
                                    </Modal.Body>
                                </Modal.Dialog>
                            </Modal>
                        </div>;
                }
                // END OF THE STAGE 2
                if (this.state.phase.idd == 2) {
                    // LAST ROUND MODAL
                    if (this.state.auction.end == true) {
                        if (this.state.player_stats.role == 0) {
                            var Results = <div>
                                <p>This was the last round. The {name_framing} has almost come to an end. In a moment we
                                    will
                                    still present you with a questionnaire.</p>
                                <p>You made a profit of {this.state.player_stats.profit} </p></div>
                        }
                        if (this.state.player_stats.role == 1) {
                            if (this.state.player_stats.penalty > 0) {
                                var missed_income = this.state.auction.retail_price * (a_units_remaining - this.state.player_stats.vouchers_negative);
                                if (a_units_remaining > 0) {
                                    var inside = <p style={{fontSize: "200%"}}>You were missing {a_units_remaining} unit(s) and
                                        therefore <strong> missed an income of {missed_income} </strong> and <strong>
                                            receive a total penalty
                                            of {penalty_rounded}.</strong></p>
                                } else {
                                    var inside = <p style={{fontSize: "200%"}}><strong> You received a total penalty
                                        of {penalty_rounded}.</strong></p>
                                }
                                var Results = <div>
                                    <p>This was the last round. The {name_framing} has almost come to an end. In a moment we
                                        will still present you with a questionnaire.</p>
                                    <p>You made a profit of {this.state.player_stats.profit} </p>
                                    {inside}
                                </div>
                            } else {
                                var Results = <div>
                                    <p>This was the last round. The {name_framing} has almost come to an end. In a moment we
                                        will still present you with a questionnaire.</p>
                                    <p>You made a profit of {this.state.player_stats.profit} </p>
                                </div>
                            }
                        }
                        // modal that presents the transition between stages
                        var Diver =
                            <div className="static-modal">
                                <Modal show="true" bsClass="pmodal" enforceFocus="true">
                                    <Modal.Dialog bsClass="pmodal-dialog">
                                        <Modal.Header bsClass="pmodal">
                                            <Modal.Title bsClass="pmodal"><b>Round {this.state.period.idd} has ended  - Results Summary</b></Modal.Title>

                                        </Modal.Header >
                                        <Modal.Body bsClass="pmodal">
                                            {Results}
                                        </Modal.Body>
                                    </Modal.Dialog>
                                </Modal>
                            </div>;
                    } else if (this.state.phase.waiting_page == true) {
                        var my_position = this.state.player_stats.vouchers_used - this.state.player_stats.vouchers_negative
                        var penalty_rounded = Math.round(this.state.player_stats.penalty_phase_total);
                        var units_remaining = my_position - this.state.player_stats.player_demand;
                        var a_units_remaining = Math.abs(units_remaining);
                        var curr_round = this.state.period.idd;

                             var history_table_indic = <span>Below, you can see your choices and outcomes in the previous rounds and the current one.</span>


                        if (this.state.player_stats.role == 0) {
                            if (this.state.player_stats.penalty_phase_total > 0) {
                                var missed_income = this.state.auction.retail_price * (a_units_remaining - this.state.player_stats.vouchers_negative);
                                var Results = <div>
                                    <p>Please take a moment to reflect on your choices and the outcomes of the
                                        market.</p>
                                    <p>You made a profit of {this.state.player_stats.profit} </p>
                                    <p style={{fontSize: "200%"}}>You have not produced {a_units_remaining} unit(s) and <strong> received a total penalty of {penalty_rounded}.</strong></p>
                                    <p>{history_table_indic}</p>
                                </div>
                            } else {
                                       var Results = <div>
                                    <p>Please take a moment to reflect on your choices and the outcomes of the
                                        market.</p>
                                    <p>You made a profit of {this.state.player_stats.profit} </p>
                                    <p>{history_table_indic}</p></div>
                            }
                        }
                        if (this.state.player_stats.role == 1) {
                            if (this.state.player_stats.penalty_phase_total > 0) {
                                var missed_income = this.state.auction.retail_price * (a_units_remaining - this.state.player_stats.vouchers_negative);
                                                                   if (a_units_remaining > 0) {
                                   var inside = <p style={{fontSize: "200%"}}> You were missing {a_units_remaining} unit(s) and therefore <strong> missed an income of {missed_income} </strong> and <strong> received a total penalty of {penalty_rounded}.</strong></p>
                                    } else {
                                    var inside = <p style={{fontSize: "200%"}}>
                                        <strong> You received a total penalty of {penalty_rounded}.</strong></p>
                                    }
                                       var Results = <div>
                                    <p>Please take a moment to reflect on your choices and the outcomes of the
                                        market.</p>
                                    <p>You made a profit of {this.state.player_stats.profit} </p>
                                            {inside}
                                    <p>{history_table_indic}</p></div>
                            } else {
                                var Results = <div>
                                    <p>Please take a moment to reflect on your choices and the outcomes of the
                                        market.</p>
                                    <p>You made a profit of {this.state.player_stats.profit} </p>
                                    <p>{history_table_indic}</p></div>
                            }
                        }
                        // modal that presents the transition between stages
                        var Diver =
                            <div className="static-modal" >
                                <Modal show="true"  bsClass="pemodal" enforceFocus="true">
                                    <Modal.Dialog bsClass="pemodal-dialog" >
                                        <Modal.Header bsClass="pemodal" id="modal_results1">
                                            <Modal.Title bsClass="pemodal" ><b>Round {this.state.period.idd} has ended  - Results Summary</b></Modal.Title>
                                        </Modal.Header >
                                        <Modal.Body id="modal_results2" bsClass="pemodal" >

                                            {Results}
                                            <HistoryTable player_id={this.state.player_id}
                                                          user_id={this.state.user_id}
                                                          auction_id={this.state.auction_id}
                                                          group_id={this.state.group_id}
                                                          history={this.state.history}
                                                          period={this.state.period}
                                                          player_stats={this.state.player_stats}
                                                          pr_no_UD = {this.state.pr_no_UD}
                                            />
                                        </Modal.Body>
                                    </Modal.Dialog>
                                </Modal>
                            </div>;

                    }
                }
            }

            // layout of the interface
            /// plot only understand fixed size, make it relative to current viewport
            var width = screen.width;
            var height = screen.height;

            // lab square
            if (width == 1280 && height == 1024) {
                 var plot_w = $(window).width() * 0.65;
                var plot_h = $(window).height() * 0.56;
            } else {
                var plot_w = $(window).width() * 0.57;
                var plot_h = $(window).height() * 0.46;
            }
            // timestamp for plot (otherwise will not refresh)
            var timest = new Date().getTime();
            var layout = <div>
                <div style={{background: "black"}}>
                    {Results_button}
                    {Diver}
                    <div
                        style={{
                            position: "absolute",
                            top: 0,
                            right: 0,
                            bottom: "98.5%",
                            left: 0,
                            background: "whitesmoke"
                        }}>
                        <Toolbar
                            timer={this.state.timer}
                            timestamp={timest}
                            player_stats={this.state.player_stats}
                            player={this.state.player}
                            phase={this.state.phase}
                            auction={this.state.auction}
                            period={this.state.period}
                            player_id={this.state.player_id}
                            user_id={this.state.user_id}
                            auction_id={this.state.auction_id}
                            group_id={this.state.group_id}
                            in_sync={this.state.in_sync}
                            educational = {this.state.educational}
                            pr_no_UD = {this.state.pr_no_UD}
                        />
                    </div>
                    <div
                        style={{
                            position: "absolute",
                            top: "3.5%",
                            right: "75%",
                            bottom: 0,
                            left: 0,
                            background: "whitesmoke",
                            margin: 1
                        }}>
                        {VoucherT}
                    </div>
                    <div
                        style={{
                            position: "absolute",
                            top: "3.5%",
                            right: "60%",
                            bottom: "50%",
                            left: "25%",
                            background: "whitesmoke",
                            margin: 1
                        }}>
                        <Trading_account mytrading={this.state.my_offers_cleared}/>
                    </div>
                    <div
                        style={{
                            position: "absolute",
                            top: "50%",
                            right: "60%",
                            bottom: "0%",
                            left: "25%",
                            background: "whitesmoke",
                            margin: 1
                        }}>
                        <Player_stats     player={this.state.player} phase_idd={this.state.phase.idd} mystats={this.state.player_stats}
                                     pr_no_UD = {this.state.pr_no_UD}  penalty={this.state.penalty} timestamp={timest} educational={this.state.educational}
                         only_spot = {this.state.only_spot}/>
                    </div>
                    <div ref="plot" id="plotdiv"
                         style={{
                             position: "absolute",
                             top: "3.5%",
                             right: "1%",
                             bottom: "47%",
                             left: "40%",
                             background: "white",
                             margin: 1
                         }}>
                        <MarketPlot all_offers={this.state.all_offers} plot_w={plot_w} plot_l={plot_h}
                                    timestamp={timest}/>
                    </div>
                    <div
                        style={{
                            position: "absolute",
                            top: "53%",
                            right: "30%",
                            bottom: "35%",
                            left: "40%",
                            background: "whitesmoke",
                            margin: 1
                        }}>
                        <MarketInfo all_offers={this.state.all_offers}/>
                    </div>
                    <div
                        style={{
                            position: "absolute",
                            top: "53%",
                            right: "1%",
                            bottom: "0",
                            left: "70%",
                            background: "whitesmoke",
                            margin: 1
                        }}>
                        <AllContractsTable contracts={this.state.active_offers}/>
                    </div>
                    <div
                        style={{
                            position: "absolute",
                            top: "65%",
                            right: "30%",
                            bottom: "20%",
                            left: "40%",
                            background: "whitesmoke",
                            margin: 1
                        }}>
                        <Submit_offer
                            auction={this.state.auction}
                            player_stats={this.state.player_stats}
                            player_id={this.state.player_id}
                            user_id={this.state.user_id}
                            auction_id={this.state.auction_id}
                            group_id={this.state.group_id}
                        />
                    </div>
                    <div
                        style={{
                            position: "absolute",
                            top: "80%",
                            right: "30%",
                            bottom: "0%",
                            left: "40%",
                            background: "whitesmoke",
                            margin: 1
                        }}>
                        <My_offers data={this.state.my_offers_standing} group_id={this.state.group_id}/>
                    </div>
                    <div style={{
                        position: "absolute",
                        top: "82.5%",
                        right: "76%",
                        bottom: 0,
                        left: "1.5%"
                    }}>
                        {Infobox}
                    </div>
                </div>
                }
            </div>;
            // end if data are loaded
        } else {
            var layout = <div> Fetching data....</div>
        }
        ;
        // render the interface
        return (
            <div>  {layout} </div>
        )
    }
});
/// Render main element to DOM
ReactDOM.render(<Auction_interface/>, document.getElementById("containerMain"));
