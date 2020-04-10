// DISPLAYS PROFIT OVERVIEW FOR THE PLAYER AND PENALTIES
// data needed
// phase_idd - idd of phase, in 2, trading result from stage 1 is displayed
// mystats - playerstats, one row with my current ones
//      role, trading_results, total_values, profit, trading_result_stage1
// penalty - list with players own penalties, id, n, amounth, id_web (pen01 string...)

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


var Penalty_row = React.createClass({
    render: function () {
        var id_name = String(this.props.id_web)
        return (<tr>
                <td id={id_name}><b>Penalty {this.props.n}:</b> {this.props.amounth}</td>
            </tr>
        )
    }
});
/// PLAYER STATS objects
var Player_stats = React.createClass({
    // dealing with penalties, changing their format as they appear, for a while
    componentWillReceiveProps: function (nextProps) {
        // if next props penalty are not zero
        if (nextProps.penalty !== null) {
            // if previous props were null, this is the first phase
            if (this.props.penalty == null) {
                // first phase
                var new_l = Object.keys(nextProps.penalty).length;
                var last_penalty_id = nextProps.penalty[new_l - 1];
                // what will happen after new penalty appears, red for a while, then black
                setTimeout(function () {
                    document.getElementById(last_penalty_id.id_web).style.color = "red";
                    ;
                }, 1500);
                // reset to normal
                setTimeout(function () {
                    document.getElementById(last_penalty_id.id_web).style.color = "black";
                    ;
                }, 5500);
            } else {
                // if not, find diff in lenghts to continue
                var new_l = Object.keys(nextProps.penalty).length;
                var old_l = Object.keys(this.props.penalty).length;
                if (new_l > old_l) {
                    var new_l = Object.keys(nextProps.penalty).length;
                    // if new list is longer then the older, new penalty line is there
                    var last_penalty_id = nextProps.penalty[new_l - 1];
                    // what will happen after new penalty appears
                    setTimeout(function () {
                        document.getElementById(last_penalty_id.id_web).style.color = "red";
                        ;
                    }, 1500);
                    // reset to normal
                    setTimeout(function () {
                        document.getElementById(last_penalty_id.id_web).style.color = "black";
                        ;
                    }, 5500);

                }
            }

        }

    },
    render: function () {
    // Components
         // Stage indicator based on educational settings
                if (this.props.educational == false) {
                    var stage_indicator1 = <span>Stage 1</span>
                    var stage_indicator = <span>(this Stage)</span>
                } else {
                   var stage_indicator1 = <span>Forward Market</span>
                   var stage_indicator = <span>(this Market)</span>
                }
        // Profit and results for RE and PR
        // different for 1st stage RE
        if (this.props.mystats.role == 1) {
            var Total_text = "Total Earnings";
            if (this.props.phase_idd == 1) {
                var total_values = "?";
                var trading_result = this.props.mystats.trading_result;
                var profit = "?";
            } else {
                var total_values = this.props.mystats.total_values;
                var trading_result = this.props.mystats.trading_result-this.props.mystats.trading_result_stage1;
                var profit = this.props.mystats.profit;
            }
        }
        if (this.props.mystats.role == 0) {
            var Total_text = "Total Cost";
            if (this.props.phase_idd == 1) {
                var total_values = this.props.mystats.total_cost;
                var trading_result = this.props.mystats.trading_result;
                var profit = this.props.mystats.profit;
            } else {
                var total_values = this.props.mystats.total_cost;
                var trading_result = this.props.mystats.trading_result-this.props.mystats.trading_result_stage1;
                var profit = this.props.mystats.profit;
            }
        }
        // Trading Revenues from prev stage if not only spot

        if (this.props.phase_idd % 2 == 0 &&  !this.props.only_spot) {
            var stage_info = <div>Trading Revenue {stage_indicator1}: {this.props.mystats.trading_result_stage1}</div>

        } else {
            var stage_info = <div></div>
        }
        // Penalty display, if penalty present
        if (this.props.penalty !== null) {
            var penalty_data = this.props.penalty.sort(sort_by("id", false, parseInt));
            var penalty_row = penalty_data.map(function (p) {
                return ( <Penalty_row
                    key={p.n}
                    amounth={p.amounth}
                    n={p.n}
                    id_web={p.id_web}
                >
                </Penalty_row>)
            });
            var penalty_map = <div>
                {penalty_row}
            </div>
        } else {
            var penalty_map = <div></div>
        }
        if (this.props.player.role == 0 & this.props.pr_no_UD == false ) {
             var penalty_indicator = <div>
            </div>
        } else {
            var penalty_indicator = <div align="center" className="panel panel-warning">
                <p><strong>
                    <table>
                        <thead></thead>
                        <tbody>
                        {penalty_map}
                        </tbody>
                    </table>
                </strong></p>
            </div>
        }
        // render elements
        return (
            <div style={{
                backgroundColor: "whitesmoke",
                position: "absolute",
                top: 0,
                bottom: 0,
                right: 0,
                left: 0,
                margin: "5px 5px 5px 0px"
            }}>
                <div style={{position: "absolute", top: 0, left: 0, bottom: "50%", right: 0}}>
                    <div className="title">Profit Overview</div>
                    <table style={{width: "100%"}}>
                        <tbody>
                        <tr>
                            <td>
                                <div align="center" className="panel panel-warning">
                                    <strong>
                                        {Total_text}: </strong> {total_values} (this round)
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <p>{stage_info}</p>
                                <div align="center" className="panel panel-warning">
                                    <p><strong>
                                        Trading Revenues: {trading_result}
                                    </strong> {stage_indicator} </p>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                {penalty_indicator}
                            </td>
                        </tr>
                        <tr>
                            <td>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
                <div style={{position: "absolute", top: "70%", left: 0, bottom: 0, right: 0}}>
                    <div className="panel panel-warning">
                        <div align="center" className="spanclass"><strong>
                            PROFIT: {profit}    </strong>(this round)
                        </div>
                    </div>
                </div>
            </div>
        )
    }
})

window.Player_stats = Player_stats;