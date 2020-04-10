// TOOLBAR AT THE TOPS
// displays the timer, etc

// connect to ReactBootstrap formating
var Navbar = ReactBootstrap.Navbar,
    Nav = ReactBootstrap.Nav,
    NavItem = ReactBootstrap.NavItem,
    NavDropdown = ReactBootstrap.NavDropdown,
    MenuItem = ReactBootstrap.MenuItem,
    Modal = ReactBootstrap.Modal,
    Button = ReactBootstrap.Button;

var Toolbar = React.createClass({
    render() {
        // LOGIC FOR SHOWING ELEMENTS
        // PLAYER INFO
        if (this.props.auction.show_ids == true) {
            var player_info = <div>
                <div className="whitefont"
                     style={{align: "right", position: "fixed", top: "2%", bottom: "90%", left: "1%", right: 0}}>
                    User ID: <strong>{this.props.player.user_id}</strong> group:<strong>{this.props.player.group_id}</strong> player_id: <strong>{this.props.player.id} </strong>
                    role: <strong>{this.props.player.role}</strong> Auction:
                    <strong>{this.props.player.auction_id}</strong>
                </div>
            </div>;
            if (this.props.phase.idd == 2) {
                if (this.props.player.role == 0 && this.props.pr_no_UD == false) {
                     var units_warning = <div></div>
                } else {
                     var units_warning = <div>
                        <h5>
                            <center><b>UNITS DEMANDED: {this.props.player_stats.player_demand}</b></center>
                        </h5>
                    </div>;
                }
            } else {
                var units_warning = <div></div>
            }

        } else {
            var player_info = <div></div>
            if (this.props.phase.idd == 2) {
                   if (this.props.player.role == 0 && this.props.pr_no_UD == false) {
                     var units_warning = <div></div>
                } else {
                     var units_warning = <div>
                        <h2>
                            <center><b>UNITS DEMANDED: {this.props.player_stats.player_demand}</b></center>
                        </h2>
                    </div>;
                }
            } else {
                var units_warning = <div></div>
            }

        }

        // TIMERS
        var timer_d = <div></div>
        if (this.props.phase.active_state == 1 & this.props.phase.idd == 1) {
            var timer_d = <div style={{display: "flex", justifyContent: "center", alignItems: "center"}}>
                <center><h4>
                    Time remaining: {this.props.timer.seconds_left}
                </h4></center>
            </div>;
        }
        if (this.props.phase.active_state == 2 && this.props.phase.idd == 1) {
            var timer_d = <div>
                <center>
                    <h5 style={{margin: 3}}>
                        <div> CONDITIONAL TIME PERIOD - Time remaining: {this.props.timer.short_seconds_left} (Make a
                            transaction to reset the clock to {this.props.auction.time_conditional})
                        </div>
                        Maximum time remaining: {this.props.timer.seconds_left}
                    </h5>
                </center>
            </div>;
        }
        if (this.props.phase.active_state == 1 && this.props.phase.idd == 2) {
            var timer_d = <div style={{display: "flex", justifyContent: "center", alignItems: "center"}}>
                <center><h4 style={{margin: 3}}>
                    Time remaining: {this.props.timer.seconds_left}
                </h4></center>
            </div>;
        }
        if (this.props.phase.active_state == 2 && this.props.phase.idd == 2) {
            if (this.props.player.role == 0 && this.props.pr_no_UD == false) {
                var timer_d = <div>
                    <center>
                        <h5 style={{margin: 3}}>
                            <div> CONDITIONAL TIME PERIOD - Time remaining: {this.props.timer.short_seconds_left}
                                (Make a
                                transaction to reset the clock to {this.props.auction.time_conditional})
                            </div>
                            Maximum time remaining: {this.props.timer.seconds_left}
                        </h5>
                    </center>
                </div>;
            } else {

                if (this.props.player_stats.units_missing > 0) {
                    var penalty = this.props.player_stats.units_missing * this.props.auction.penalty_perunit;
                    if (this.props.player.role == 0) {
                        var timer_d = <div>
                            <center>
                                <h5 style={{margin: 3}}>
                                    <div> CONDITIONAL TIME PERIOD - Time
                                        remaining: {this.props.timer.short_seconds_left}
                                        (Make a
                                        transaction to reset the clock to {this.props.auction.time_conditional})
                                    </div>

                                    Maximum time remaining: {this.props.timer.seconds_left} <span
                                    style={{backgroundColor: "red"}}>(Sell another {this.props.player_stats.units_missing}
                                    unit(s) to avoid penalty of {this.props.player_stats.units_missing}
                                    x {this.props.auction.penalty_perunit} = {penalty} ECU)</span>
                                </h5>
                            </center>
                        </div>;
                    } else {
                        var timer_d = <div>
                            <center>
                                <h5 style={{margin: 3}}>
                                    <div> CONDITIONAL TIME PERIOD - Time
                                        remaining: {this.props.timer.short_seconds_left}
                                        (Make a
                                        transaction to reset the clock to {this.props.auction.time_conditional})
                                    </div>

                                    Maximum time remaining: {this.props.timer.seconds_left} <span
                                    style={{backgroundColor: "red"}}>(Buy another {this.props.player_stats.units_missing}
                                    unit(s) to avoid penalty of {this.props.player_stats.units_missing}
                                    x {this.props.auction.penalty_perunit} = {penalty} ECU)</span></h5>
                            </center>
                        </div>;

                    }
                } else {
                    var timer_d = <div>
                        <center>
                            <h4 style={{margin: 3}}>
                                <div> CONDITIONAL TIME PERIOD - Time remaining: {this.props.timer.short_seconds_left}
                                    (Make
                                    a
                                    transaction to reset the clock to {this.props.auction.time_conditional})
                                </div>
                                Maximum time remaining: {this.props.timer.seconds_left}              </h4>
                        </center>

                    </div>;
                }
            }
        }
        if (this.props.phase.active_state == 3 && this.props.phase.idd == 2) {
            if (this.props.player.role == 0 && this.props.pr_no_UD == false) {

                  var timer_d = <div>
                <center>
                    <h5 style={{margin: 3}}>
                        Maximum time remaining: {this.props.timer.seconds_left}
                    </h5>
                </center>
            </div>;
            } else {

            if (this.props.player_stats.units_missing > 0) {
                var penalty = this.props.player_stats.units_missing * this.props.auction.penalty_perunit;
                if (this.props.player.role == 0) {
                    if (this.props.timer.seconds_left > this.props.auction.time_conditional) {
                        var timer_d = <div>
                            <center>
                                <h5 style={{margin: 3}}>
                                    <div> PENALTY TIME PERIOD - Time
                                        remaining {this.props.timer.short_seconds_left} <span
                                            style={{backgroundColor: "red"}}> (Sell another {this.props.player_stats.units_missing}
                                            unit(s) to avoid penalty
                       of {this.props.player_stats.units_missing} x {this.props.auction.penalty_perunit} = {penalty}
                                            ECU)
                  </span></div>
                                    Maximum time remaining: {this.props.timer.seconds_left} (Will end when nobody has
                                    missing units)
                                </h5>
                            </center>
                        </div>;
                    } else {

                        var timer_d = <div>
                            <center>
                                <h5 style={{margin: 3}}>
                                    <div> PENALTY TIME PERIOD - Time
                                        remaining {this.props.timer.short_seconds_left} <span
                                            style={{backgroundColor: "red"}}> (Sell another {this.props.player_stats.units_missing}
                                            units to avoid the end-penalty)
                  </span></div>
                                    Maximum time remaining: {this.props.timer.seconds_left} (Will end when nobody has
                                    missing units)
                                </h5>
                            </center>
                        </div>;
                    }

                } else {
                    if (this.props.timer.seconds_left > this.props.auction.time_conditional) {
                        var timer_d = <div>
                            <center>
                                <h5 style={{margin: 3}}>
                                    <div>PENALTY TIME PERIOD - Time
                                        remaining {this.props.timer.short_seconds_left} <span
                                            style={{backgroundColor: "red"}}>
                      (Buy another {this.props.player_stats.units_missing} unit(s) to avoid penalty
                       of {this.props.player_stats.units_missing} x {this.props.auction.penalty_perunit} = {penalty}
                                            ECU)
                  </span></div>
                                    Maximum time remaining: {this.props.timer.seconds_left} (Will end when nobody has
                                    missing units)
                                </h5>
                            </center>
                        </div>;
                    } else {
                        var timer_d = <div>
                            <center>
                                <h5 style={{margin: 3}}>
                                    <div>PENALTY TIME PERIOD - Time
                                        remaining {this.props.timer.short_seconds_left} <span
                                            style={{backgroundColor: "red"}}>
                      (Sell another {this.props.player_stats.units_missing} unit(s) to avoid the end-penalty)
                  </span></div>
                                    Maximum time remaining: {this.props.timer.seconds_left} (Will end when nobody has
                                    missing units)
                                </h5>
                            </center>
                        </div>;
                    }
                }
            } else {
                var timer_d = <div>
                    <center>
                        <h4 style={{margin: 3}}>
                            <div> PENALTY TIME PERIOD</div>
                            Maximum time remaining: {this.props.timer.seconds_left} (Will end when nobody has missing
                            units)
                        </h4>
                    </center>
                </div>;
            }
        }
    }
        // Stage indicator based on educational settings
        if (this.props.educational == false) {
            var stage_indicator = <span> Stage: {this.props.phase.idd} </span>
        } else {
            if (this.props.phase.idd == 1) {
                    var stage_indicator = <span> Forward Market </span>
            } else {
                    var stage_indicator = <span> Spot Market </span>
            }
        }
        return (
            <div>
                <Nav className="navbar navbar-inverse navbar-fixed-top" bsStyle="tabs">
                    <div>
                        {player_info}
                        <div className="whitefont"
                             style={{
                                 textAlign: "left",
                                 position: "fixed",
                                 top: "0%",
                                 bottom: "90%",
                                 left: "20%",
                                 right: "20%"
                             }}>

                            {timer_d}
                        </div>
                        <div className="whitefont"
                             style={{
                                 textAlign: "left",
                                 position: "fixed",
                                 top: "0%",
                                 bottom: "90%",
                                 left: "5%",

                             }}>
                            <center> {units_warning} </center>
                        </div>
                        <div className="whitefont"
                             style={{
                                 textAlign: "right",
                                 position: "fixed",
                                 top: 0,
                                 bottom: "95%",
                                 left: "80%",
                                 right: "1%"
                             }}>
                            <h4 style={{margin: 5}}> ROUND: {this.props.period.idd}  &nbsp;
                                {stage_indicator} </h4> {this.props.in_sync}
                        </div>
                    </div>
                </Nav>
            </div>
        );
    }
});

window.Toolbar = Toolbar;