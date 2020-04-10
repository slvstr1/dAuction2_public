/** create admin table in REACT for MASTER page **/
var refresh = document.getElementById("myVar").value;

// sorts array
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

var Player_table_row = React.createClass({
    render: function () {
        return (
            <tr>
                <td>
                    <center>{this.props.order}</center>
                </td>
                <td>
                    <center>{this.props.user_id}</center>
                </td>
                <td>
                    <center>{this.props.ip}</center>
                </td>
                <td>
                    <center>{this.props.selected}</center>
                </td>
                <td>
                    <center>{this.props.auction}</center>
                </td>
                <td>
                    <center>{this.props.group}</center>
                </td>
                <td>
                    <center>{this.props.role}</center>
                </td>
                <td>
                    <center>{this.props.testing_correct}</center>
                </td>
                <td>
                    <center>{this.props.testing_errors}</center>
                </td>
                <td>
                    <center>{this.props.app}</center>
                </td>
                <td>
                    <center>{this.props.state}</center>
                </td>
                <td>
                    <center>{this.props.page}</center>
                </td>
                <td>
                    <center>{this.props.player_ready}</center>
                </td>
                <td>
                    <center>{this.props.last_alive}</center>
                </td>
                <td>
                    <center>{this.props.need_refreshing}</center>
                </td>

            </tr>
        )
    }
});


var Player_table = React.createClass({
    // set init. state to empty
    getInitialState: function () {
        return {
            data_players: [],
            data_timer: [],
            data_auction: [],
            data_period: [],
            data_phase: [],
            data_cache: [],
        };
    },
    fetchPlayerData: function () {
        $.get("/ajax_admin", function (data) {
            if (this.isMounted()) {
                // if not input, generate default
                if (typeof data.tt != "undefined") {
                    var timer_data = data.tt
                } else {
                    var timer_data = {runnning: false, seconds_left: ""}
                }
                if (typeof data.period != "undefined") {
                    var period_data = data.period
                } else {
                    var period_data = {idd: ""}
                }
                if (typeof data.phase != "undefined") {
                    var phase_data = data.phase
                } else {
                    var phase_data = {idd: "", question_page: false, waiting_page: false}
                }
                if (typeof data.cache_duration != "undefined") {
                    var cache_duration_data = data.cache_duration
                } else {
                    var cache_duration_data = "N/A"
                }
                this.setState({
                    data_timer: timer_data,
                    data_players: data.players,
                    data_auction: data.auction,
                    data_period: period_data,
                    data_phase: phase_data,
                    data_cache: cache_duration_data
                });
            }
        }.bind(this));
    },
    componentDidMount: function () {
        this.fetchPlayerData();
        setInterval(function () {
            this.fetchPlayerData();
        }.bind(this), refresh);
    },
    render: function () {
        // order and number players before parsing them
        var manipulate_sorted = this.state.data_players;
        var order_start = 1
        for (var key in manipulate_sorted) {
            if (manipulate_sorted.hasOwnProperty(key)) {
                manipulate_sorted[key].order = order_start;
                var order_start = order_start + 1
            }
        }
        var tablerows = manipulate_sorted.map(function (player) {
            // logic for looping, replace values of variables with "labels"
            if (player.player_ready == false) {
                player.player_ready = "False"
            }
            if (player.player_ready == true) {
                player.player_ready = "True"
            }
            if (player.page_need_refreshing == false) {
                player.page_need_refreshing = "-"
            }
            if (player.page_need_refreshing == true) {
                player.page_need_refreshing = "!"
            }
            if (player.selected == false) {
                player.selected = "False"
            }
            if (player.selected == true) {
                player.selected = "True"
            }
            if (player.role == 1) {
                player.role = "RE"
            }
            if (player.role == 0) {
                player.role = "PR"
            }
            if (player.app == 0) {
                player.app = "NONE"
            }
            if (player.app == 1) {
                player.app = "INSTR"
            }
            if (player.app == 2) {
                player.app = "DISTR"
            }
            if (player.app == 3) {
                player.app = "TEST"
            }
            if (player.app == 4) {
                player.app = "FS"
            }
            if (player.app == 5) {
                player.app = "QUEST"
            }
            if (player.app == 6) {
                player.app = "PAYOUT"
            }
            if (player.state == 1) {
                player.state = "WAIT"
            }
            if (player.state == 2) {
                player.state = "WORK"
            }
            if (player.state == 3) {
                player.state = "FIN"
            }
            return ( <Player_table_row
                    user_id={player.user_id }
                    key={player.id}
                    order={player.order}
                    selected={player.selected}
                    auction={player.auction_id}
                    group={player.group_id}
                    ip={player.user.ip}
                    role={player.role}
                    testing_errors={player.testing_errors}
                    testing_correct={player.testing_correct}
                    app={player.app}
                    state={player.state}
                    page={player.page}
                    player_ready={player.player_ready}
                    last_alive={player.last_alive}
                    need_refreshing={player.page_need_refreshing}
                > </Player_table_row>
            )
        });
        var timer_running = "N/A";
        if (this.state.data_timer.running == true) {
            var timer_running = "True";
        }
        if (this.state.data_timer.running == false) {
            var timer_running = "False";
        }

        var transition = "asdasda";
        var wp = this.state.data_phase.waiting_page;
        var qp = this.state.data_phase.question_page;
        if (wp == false && qp == false) {
            var transition = "";
        } else if (wp == true && qp == true) {
            var transition = "";
        } else if (wp == true) {
            var transition = ", waiting";
        } else if (qp == true) {
            var transition = ", question";
        }
        if (this.state.data_phase.question_page == true && this.state.data_phase.question_page != true) {
            var transition = ", question";
        }
        if (this.state.data_phase.waiting_page == true && this.state.data_phase.question_page != true) {
            var transition = ", waiting";
        }

        return (
            <div className="col-4">
                <div style={{display: "inline"}}>
                    <p>Timer from auction: {this.state.data_timer.seconds_left} , Is running: {timer_running}</p>
                    <p>Present period: {this.state.data_period.idd} , Present
                        Phase: {this.state.data_phase.idd}{transition}, Present
                        State: {this.state.data_phase.active_state} </p>
                    <p>Cache duration: {this.state.data_cache}</p>
                </div>
                <table id="ajax_table" className="table table-striped table-condensed">
                    <thead>
                    <tr>
                        <th>#</th>
                        <th>User ID</th>
                        <th>IP</th>
                        <th>Slctd</th>
                        <th>Auct</th>
                        <th>group</th>
                        <th>role</th>
                        <th>t_cor</th>
                        <th>t_err</th>
                        <th>App</th>
                        <th>State</th>
                        <th>Page</th>
                        <th>Ready</th>
                        <th>LastA</th>
                        <th>Rfrsh</th>
                    </tr>
                    </thead>
                    <tbody>
                    {tablerows}
                    </tbody>
                </table>
            </div>
        )
    }
});
ReactDOM.render(<Player_table/>, document.getElementById("Player_table"));

