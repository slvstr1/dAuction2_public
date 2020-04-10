// Market plot interface for exploration of the data
// used function
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
// buttons
var Button = React.createClass({
    render: function () {
        return (
            <button
                value={this.props.value}
                onClick={this.props.function}
                className={this.props.className}
            >
                {this.props.display}
            </button>
        )
    }
});
/*
 Plot data docs:
 1. get data from the parser, use relative_time to get relative times of offers within period/phase, load them to STATE
 state -> offers, periods, phases, groups
 2. create buttons for groups and periods (there is no default group or period for now)
 3. after selection of the period and group, dynamically create Phase buttons
 */
// main element
var Market = React.createClass({
    getInitialState: function () {
        return {
            // initial state from parser
            offers: [],
            periods: [],
            phases: [],
            groups: [],

            // current data selected by the buttons
            cur_group: [],
            cur_period: [],
            cur_phase: [],
            cur_offers: [],

            // results -> offers to display
            display_offers: [],
            // filtered offers from display offers, filtered by using slider
            filtered_offers: [],

            time: "N/A",
            per_selected: 0,
            phase_selected: 0,
            speed: 1000,
            play_indic: "",
            data_msg: "",
            data_live: 0,
            auction: "",
            group_selected: 0,
            offers_g: [],
            offers_pe: [],
            offers_pha: [],
        };
    },
    // set current props to state for editing
    propsToState: function () {
        console.log("trigger")
        this.setState({
            periods: this.props.periods,
            phases: this.props.phases,
            offers: this.props.offers,
            groups: this.props.group
        });
    },
    // compute duration of periods/phase, time of clearing/creation of offer in respective period/phase
    relativeTime: function () {
        // make shortcuts to data from react
        var periods = this.state.periods;
        var offers = this.state.offers;
        var phases = this.state.phases;
        var groups = this.state.groups;
        // loop for every period
        for (var key in periods) {
            if (periods.hasOwnProperty(key)) {
                // select phases for looped period
                var per_phases = $.grep(phases, function (n, i) {
                    return n.period == periods[key].id;
                });
                // sort them
                per_phases.sort(sort_by("idd", false, parseInt));

                // PERIOD and PHASES
                // should be only 2, select the first one and make it the start of period
                periods[key].start = per_phases[0].created
                periods[key].end = periods[key].updated
                periods[key].dura = (periods[key].end - periods[key].start ) / 1000
                // S1
                // start of S1 is its creation
                per_phases[0].start = per_phases[0].created
                // end of S1 is creation of S2
                per_phases[0].end = per_phases[1].created
                per_phases[0].dura = (per_phases[0].end - per_phases[0].start) / 1000
                per_phases[1].start = per_phases[1].created
                // end of S2 is the end of the period
                per_phases[1].end = periods[key].end;
                per_phases[1].dura = (per_phases[1].end - per_phases[1].start) / 1000;

                // OFFERS
                var period_offers = $.grep(offers, function (n, i) {
                    return (n.phase == per_phases[0].id || n.phase == per_phases[1].id);
                });
                for (var k in period_offers) {
                    if (period_offers.hasOwnProperty(k)) {
                        // time cleared and created in period
                        if (period_offers[k].cleared == true) {
                            period_offers[k].per_clear = ( period_offers[k].timeCleared - periods[key].start) / 1000;
                        } else {
                            period_offers[k].per_clear = ""
                        }
                        period_offers[k].per_created = (period_offers[k].created - periods[key].start) / 1000;
                        // time cleared and created in PHASE 1 (STAGE 1)
                        if (period_offers[k].phase == per_phases[0].id) {
                            if (period_offers[k].cleared == true) {
                                period_offers[k].pha_clear = ( period_offers[k].timeCleared - per_phases[0].start ) / 1000;
                            } else {
                                period_offers[k].pha_clear = ""
                            }
                            period_offers[k].pha_created = (period_offers[k].created - per_phases[0].start) / 1000;
                        }
                        // time cleared and created in PHASE 2 (STAGE 2)
                        if (period_offers[k].phase == per_phases[1].id) {
                            if (period_offers[k].cleared == true) {
                                period_offers[k].pha_clear = (period_offers[k].timeCleared - per_phases[1].start ) / 1000;
                            } else {
                                period_offers[k].pha_clear = ""
                            }
                            period_offers[k].pha_created = (period_offers[k].created - per_phases[1].start) / 1000;
                        }
                    }
                }
            }
        }
        // update state
        this.setState({
            periods: periods,
            phases: phases,
            offers: offers,
            groups: groups
        });

    },
    offerFilter: function (caller, value) {
        var group = this.state.cur_group
        var period = this.state.cur_period
        var phase = this.state.cur_phase
        // state updates after function is executed, paste update of the calling function to this function
        if (caller == "g") {
            var group = value
        } else if (caller == "pe") {
            var period = value
        } else if (caller == "ph") {
            var phase = value
        }
        if (group.length == 0 | period.length == 0 | phase.length == 0) {
            //pass
            //console.log("passing", group.length, period.length, phase.length)
        } else {
            // filter offers
            var group_id = group.id
            var period_id = period.id
            var cur_phases = $.grep(this.state.phases, function (n, i) {
                return n.period == period_id;
            });
            var phase_id_1 = cur_phases[0].id;
            var phase_id_2 = cur_phases[1].id;
            if (phase == "1") {
                var cur_offers = $.grep(this.state.offers, function (n, i) {
                    return (n.phase == phase_id_1 & n.group == group_id);
                });
                  this.setState({
                time: cur_phases[0].dura,
                });
                   // enable slider
                $("#slider").prop('disabled', false);
                $("#slider").prop('max', cur_phases[0].dura);
                $("#slider").prop('value', cur_phases[0].dura);
                // enable buttons
                $("#play_btn").removeClass("disabled");
                $("#stop_btn").removeClass("disabled");
                $("#play_start_btn").removeClass("disabled");
                this.btnStop()
            }
            if (phase == "2") {
                var cur_offers = $.grep(this.state.offers, function (n, i) {
                    return (n.phase == phase_id_2 & n.group == group_id);
                });
                     this.setState({
                time: cur_phases[1].dura,
                });
                // enable slider
                $("#slider").prop('disabled', false);
                $("#slider").prop('max', cur_phases[1].dura);
                $("#slider").prop('value', cur_phases[1].dura);
                // enable buttons
                $("#play_btn").removeClass("disabled");
                $("#stop_btn").removeClass("disabled");
                $("#play_start_btn").removeClass("disabled");
                this.btnStop()
            }
            if (phase == "1+2") {
                var cur_offers = $.grep(this.state.offers, function (n, i) {
                    return ((n.phase == phase_id_1 | n.phase == phase_id_2) & n.group == group_id);
                });
                var period_dura = cur_phases[1].dura +cur_phases[0].dura
                        this.setState({
                time: period_dura,
                });
                // enable slider
                $("#slider").prop('disabled', false);
                $("#slider").prop('max', period_dura);
                $("#slider").prop('value', period_dura);
                // enable buttons
                $("#play_btn").removeClass("disabled");
                $("#stop_btn").removeClass("disabled");
                $("#play_start_btn").removeClass("disabled");
                this.btnStop()
            }
            this.setState({
                filtered_offers: cur_offers,
                display_offers: cur_offers
            });
        }
    },

    // SELECT FUNCTIONS
    groupSelect: function (e) {
        var cur_group = $.grep(this.state.groups, function (n, i) {
            return n.id == e.target.value;
        });
        this.setState({
            cur_group: cur_group[0],
        });
        this.offerFilter("g", cur_group[0])
    },
    periodSelect: function (e) {
        var cur_period = $.grep(this.state.periods, function (n, i) {
            return n.id == e.target.value;
        });
        this.setState({
            cur_period: cur_period[0],
        });
        this.offerFilter("pe", cur_period[0])
    },
    phaseSelect: function (e) {
        this.setState({
            cur_phase: e.target.value,
        });
        this.offerFilter("ph", e.target.value)
    },

    // function of change of slider value
    slider_change: function (e) {
        var slider_time = e.target.value
        // filter offers
        var offers = JSON.parse(JSON.stringify(this.state.filtered_offers));
        var new_offers = []
        // filter offers, if offer is created in time period and if its cleared after time period, change to ontcleared
        for (var key in offers) {
            if (offers.hasOwnProperty(key)) {
                // for period or 1+2 phases
                if (this.state.cur_phase == "1+2") {
                    if (slider_time >= offers[key].per_created) {
                        if (slider_time < offers[key].per_clear) {
                            offers[key].cleared = false
                            offers[key].unitsAvailable = offers[key].unitsCleared
                            new_offers.push(offers[key])
                        } else {
                            new_offers.push(offers[key])
                        }
                    }
                    // for phases
                } else {
                    if (slider_time >= offers[key].pha_created) {
                        if (slider_time < offers[key].pha_clear) {
                            offers[key].cleared = false
                            offers[key].unitsAvailable = offers[key].unitsCleared
                            new_offers.push(offers[key])
                        } else {
                            new_offers.push(offers[key])
                        }
                    }
                }

            }

        }
        this.setState({
            time: slider_time,
            display_offers: new_offers
        });
    },
    // function for the play button
    btnPlay: function (e) {
        if (window.checker == false && this.state.cur_period.idd != "N/A") {
            if (e.target.value == "normal") {
                if ((this.state.phase_selected == 0 && this.state.time != this.state.cur_period.dura)
                    || (this.state.phase_selected == 1 && this.state.time < this.state.cur_phase.dura)) {
                    this.setState({
                        play_indic: "(playing)",
                    });
                    this.innerPlay()

                }
            }
            if (e.target.value == "start") {
                $("#slider").prop('value', 0);
                clearInterval(window.playInterval);
                this.setState({
                    time: 0,
                    play_indic: "(playing)",
                });
                this.innerPlay()
            }
        }
    },
    innerPlay: function () {
        // speed of change
        var speed = this.state.speed;
        // create named interval with interrupts
        window.rep = 0
        window.checker = true
        window.playInterval = setInterval(function () {
            window.rep = window.rep + 1
            var cur_value = parseInt($("#slider").prop('value'))
            var max_value = parseInt($("#slider").prop('max'))
            var diff = max_value - cur_value
            // steps
            var ticks = 1
            if (diff > 0) {
                if (rep == 1) {
                    var fut_value = Math.round(parseInt($("#slider").prop('value')) / ticks) * ticks
                    $("#slider").prop('value', fut_value)
                    this.setState({
                        time: fut_value,
                    });
                    var hack = {'target': {'value': fut_value}}
                    this.slider_change(hack)
                } else if (diff <= ticks) {
                    var fut_value = max_value
                    $("#slider").prop('value', fut_value)
                    this.setState({
                        time: fut_value,
                    });
                    var hack = {'target': {'value': fut_value}}
                    this.slider_change(hack)
                    clearInterval(window.playInterval);
                    window.checker = false
                    this.setState({

                        play_indic: "",
                    });
                } else {
                    var fut_value = cur_value + ticks
                    $("#slider").prop('value', fut_value)
                    this.setState({
                        time: fut_value,
                    });
                    var hack = {'target': {'value': fut_value}}
                    this.slider_change(hack)

                }
            }
        }.bind(this), speed);


    },
    // function for stop buttn
    btnStop: function (e) {
        if (window.checker == true) {
            clearInterval(window.playInterval);
            window.checker = false
            $("#play_btn").removeClass("disabled");
            $("#play_start_btn").removeClass("disabled");
        }
        this.setState({
            play_indic: "",
        });
    },
    btnSpeed: function (e) {
        var up_bound = 5000
        var tick = 100
        var changed_speed = this.state.speed
        if (this.state.speed > 200) {
            if (e.target.value == "plus") {
                var changed_speed = this.state.speed - tick
                if (window.checker == true) {
                    clearInterval(window.playInterval);
                    window.checker = false
                    this.btnPlay({'target': {'value': "normal"}})
                }
            }
        }
        if (this.state.speed < up_bound) {
            if (e.target.value == "minus") {
                var changed_speed = this.state.speed + tick
            }
            if (window.checker == true) {
                clearInterval(window.playInterval);
                window.checker = false
                this.btnPlay({'target': {'value': "normal"}})
            }
        }
        this.setState({
            speed: changed_speed,
        });


    },
    // function for reset button
    btnReset: function (e) {
        clearInterval(window.playInterval);
        window.checker = false
        $("#slider").prop('value', 0);
        $("#slider").prop('disabled', true);
        $("#play_start_btn").addClass("disabled");
        this.setState({
            cur_period: {idd: 'N/A', total_demand: 'N/A', dura: "N/A"},
            cur_phases: [],
            cur_phase: {idd: 'N/A', dura: "N/A"},
            cur_offers: [],
            d_offers: [],
            map_phases: [],
            time: "N/A",
            phase_selected: 0,
            per_selected: 0,
            group_selected: 0,
            speed: 1000,
            play_indic: ""
        })
    },


    // execute when all its loaded, only once
    componentWillMount: function () {
        setTimeout(function () {
            this.propsToState();
        }.bind(this), 2000);
        setTimeout(function () {
            this.relativeTime();
        }.bind(this), 3000);
        window.checker = false
    },
    componentDidMount: function () {
    },

    render () {
        // BUTTONS:
        // groups
        var groups_copy = this.props.group;
        for (var key in groups_copy) {
            if (groups_copy.hasOwnProperty(key)) {
                groups_copy[key].className = "btn btn-small";
                groups_copy[key].onClick = this.groupSelect;
            }

        }
        var Map_groups = groups_copy.map(function (e) {
            return ( <Button
                key={e.idd}
                value={e.id}
                display={e.idd}
                function={e.onClick}
                className={e.className}
            >
            </Button>)
        });
        // periods
        var periods_copy = JSON.parse(JSON.stringify(this.state.periods));
        periods_copy.sort(sort_by("idd", false, parseInt));
        for (var key in periods_copy) {
            if (periods_copy.hasOwnProperty(key)) {
                periods_copy[key].className = "btn btn-small";
                periods_copy[key].onClick = this.periodSelect;
            }
        }
        var Map_periods = periods_copy.map(function (e) {
            return ( <Button
                key={e.idd}
                value={e.id}
                display={e.idd}
                function={e.onClick}
                className={e.className}
            >
            </Button>)
        });
        // phases
        var Phase_buttons =
            <div className="btn-group btn-default">
            <button value="1" onClick={this.phaseSelect} className="btn btn-small" > 1 </button>
            <button value="2" onClick={this.phaseSelect} className="btn btn-small" > 2 </button>
            <button value="1+2"  onClick={this.phaseSelect} className="btn btn-small"> 1+2 </button>
            </div>

        var time_slider = String(this.state.time)
        var plot_w = $(window).width() * 0.8;
        var plot_h = $(window).height() * 0.6;

        // timestamp for plot (otherwise will not refresh)
        var timest = new Date().getTime();

        // SELECT INFOTEXT
        if (this.state.cur_group.length == 0) {
            var group_text = <div className="alert-danger container"><b> SELECT GROUP </b></div>
        } else {
            var group_text = <div><b>GROUP:</b> {this.state.cur_group.idd}</div>
        }

        if (this.state.cur_period.length == 0) {
            var per_text = <div className="alert-danger container"><b> SELECT PERIOD </b></div>
        } else {
            var per_text = <div><b>PERIOD:</b> {this.state.cur_period.idd} Duration: {this.state.cur_period.dura}</div>
        }

        if (this.state.cur_phase.length == 0) {
            var phase_text = <div className="alert-danger container"><b> SELECT PHASE </b></div>
        } else {
            if (this.state.cur_phase == "1+2") {
                var phase_text = <div className="alert-warning">Data for all phases in period loaded, select phase
                    bellow
                    for separation</div>
            } else {
                var phase_text = <div><b>PHASE:</b> {this.state.cur_phase}
                </div>
            }
        }

        // check if finished
        if ((this.state.time == this.state.cur_period.dura) || (this.state.phase_selected == 1 && this.state.time == this.state.cur_phase.dura)) {
            //   console.log("fire!")
            $("#play_btn").addClass("disabled");
            $("#stop_btn").addClass("disabled");
        } else {
            $("#play_btn").removeClass("disabled");
            $("#stop_btn").removeClass("disabled");
        }

        // if playing
        if (window.checker == true) {
            $("#play_btn").addClass("disabled");
            $("#play_start_btn").addClass("disabled");

        } else {
            $("#stop_btn").addClass("disabled");
        }

        var speed_display = parseFloat(Math.round((1000 / this.state.speed) * 100) / 100).toFixed(2);

        return (
            <div className="row container-fluid">
                <div id="plot" className="row container-fluid">
                    <div className="col-lg-12">
                        <MarketPlot all_offers={this.state.display_offers} plot_w={plot_w} plot_l={plot_h}
                                    timestamp={timest}/>
                    </div>
                </div>
                <div id="details" className="row container-fluid">
                    <div className="col-lg-12">
                        <div className="container-fluid row">
                            <input defaultValue="0" id="slider" type="range" name="time" min="0" max="10" step="1"
                                   disabled="true" onChange={this.slider_change}/>
                            <b> Time:</b> {time_slider} {this.state.play_indic}
                        </div>
                        <div className="row container-fluid">
                            <button
                                id="play_start_btn"
                                onClick={this.btnPlay}
                                className="btn btn-info btn-lg disabled"
                                value="start"
                            >
                                PLAY from the start
                            </button>
                            <button
                                id="play_btn"
                                onClick={this.btnPlay}
                                className="btn btn-primary btn-lg disabled"
                                value="normal"

                            >
                                PLAY from now
                            </button>
                            <button
                                id="play_btn"
                                onClick={this.btnSpeed}
                                className="btn btn-primary"
                                value="plus"

                            >
                                +
                            </button>
                            <button
                                id="play_btn"
                                onClick={this.btnSpeed}
                                className="btn disabled"
                                value="minus"

                            >
                                Tick rate per s: {speed_display}
                            </button>

                            <button
                                id="play_btn"
                                onClick={this.btnSpeed}
                                className="btn btn-primary"
                                value="minus"

                            >
                                -
                            </button>

                            <button
                                id="stop_btn"
                                onClick={this.btnStop}
                                className="btn btn-secondary btn-lg btn-danger disabled"

                            >
                                STOP at cur. time
                            </button>


                            <button
                                onClick={this.btnReset}
                                className="btn btn btn-secondary btn-warning btn-lg"
                            >
                                RESET ALL
                            </button>
                        </div>
                    </div>
                </div>
                <div id="menu" className="row container-fluid">
                    <div className="col-lg-12">
                        <div id="per_select">
                            {group_text}
                        </div>
                        <div>
                            {Map_groups}
                        </div>
                        <div id="per_select">
                            {per_text}
                        </div>
                        <div id="menu" className="row container-fluid">
                            <div className="btn-group btn-default">
                                {Map_periods}
                            </div>
                        </div>
                        <div id="phase_select">
                            {phase_text}
                        </div>
                        <div id="menu" className="row container-fluid">
                            {Phase_buttons}
                        </div>
                    </div>

                </div>
            </div>
        )
    }
});

window.Market = Market