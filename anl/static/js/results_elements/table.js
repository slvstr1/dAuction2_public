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

function getMedian(args) {
    if (!args.length) {
        return 0
    }
    ;
    var numbers = args.slice(0).sort((a, b) => a - b);
    var middle = Math.floor(numbers.length / 2);
    var isEven = numbers.length % 2 === 0;
    return isEven ? (numbers[middle] + numbers[middle - 1]) / 2 : numbers[middle];
}

function average(data) {
    var sum = data.reduce(function (sum, value) {
        return sum + value;
    }, 0);
    var avg = sum / data.length;
    return avg;
}

var Table_row = React.createClass({
    render: function () {
        return (<tr scope="row">
                <td>{this.props.period_id}</td>
                <td>{this.props.group_id}</td>
                <td>{this.props.price_forward}</td>
                <td>{this.props.q_forward}</td>
                <td>{this.props.demand}</td>
                <td>{this.props.price_spot}</td>
                <td>{this.props.q_spot}</td>
                <td>{this.props.profit}</td>
            </tr>
        )
    }
});


var Table_main = React.createClass({
    render() {
        var auction = this.props.auction;
        var periods = this.props.periods.sort(sort_by("id", false, parseInt));
        var groups = this.props.group.sort(sort_by("id", false, parseInt));
        // rename ids to group_id and period_id
        for (var key in  periods) {
            if (periods.hasOwnProperty(key)) {
                periods[key].period_id = periods[key].id
                periods[key].period_idd = periods[key].idd
            }
        }
        for (var key in  groups) {
            if (groups.hasOwnProperty(key)) {
                groups[key].group_id = groups[key].id
                groups[key].group_idd = groups[key].idd
            }
        }
        // create table rows, one row per group and period - round
        var rows = [];
        for (var key in  periods) {
            if (periods.hasOwnProperty(key)) {
                for (var key2 in  groups) {
                    if (groups.hasOwnProperty(key2)) {
                        rows.push(Object.assign([], periods[key], groups[key2]))
                    }
                }
            }
        }
        // create summary statistic by looping trough objects and saving to respective rows (group/period combination)
        for (var key in rows) {
            if (rows.hasOwnProperty(key)) {

                // PLAYER STATS
                let player_stats = $.grep(this.props.player_stats, function (n, i) {
                    return (n.period == rows[key].period_id && n.group == rows[key].group_id);
                });
                var demand = 0;
                var vouchers = [[], []];
                var vouchers2 = [[], []];
                var profit = [[], []];
                for (var key2 in player_stats) {
                    if (player_stats.hasOwnProperty(key2)) {
                        // players position, PRODUCER
                        if (player_stats[key2].role == 0) {
                            // player position
                            vouchers[0].push(player_stats[key2].vouchers_used_stage1 - player_stats[key2].vouchers_negative_stage1)
                            vouchers2[0].push(player_stats[key2].vouchers_used - player_stats[key2].vouchers_negative)
                            // profit sign
                            if (player_stats[key2].profit > 0) {
                                profit[0].push("+")
                            } else {
                                profit[0].push("-")
                            }
                            // RETAILER
                        } else {
                            // player position
                            vouchers[1].push(player_stats[key2].vouchers_used_stage1 - player_stats[key2].vouchers_negative_stage1)
                            vouchers2[1].push(player_stats[key2].vouchers_used - player_stats[key2].vouchers_negative)
                            // MARKET units demanded in each round
                            var demand = demand + player_stats[key2].player_demand
                            // profit sign
                            if (player_stats[key2].profit > 0) {
                                profit[1].push("+")
                            } else {
                                profit[1].push("-")
                            }
                        }
                    }
                }
                // save to ROWS object
                rows[key].profit = "[" + String(profit[0]) + "]" + "[" + String(profit[1]) + "]"
                // divide by four to get individual units demanded
                rows[key].demand = String(demand) + "/" + String(demand / 4);
                rows[key].q_spot = "[" + String(vouchers2[0]) + "][" + String(vouchers2[1]) + "]"
                rows[key].q_forward = "[" + String(vouchers[0]) + "][" + String(vouchers[1]) + "]";

                // PHASES - STAGES
                var phases = $.grep(this.props.phases, function (n, i) {
                    return (n.period == rows[key].period_id);
                });
                // initialize values
                // collect prices as arrays, will be averaged/medianed?? medied??
                var price_spot = [];
                var price_forward = [];
                var q_spot = 0;
                var q_forward = 0;
                for (var key3 in phases) {
                    if (phases.hasOwnProperty(key3)) {
                        // FORWARD - STAGE 1
                        if (phases[key3].idd == 1) {
                            // filter offers made in each phase, that were cleared
                            let offers = $.grep(this.props.offers, function (n, i) {
                                return (n.phase == phases[key3].id & n.group == rows[key].group_id & n.cleared == true);
                            })
                            for (var key5 in offers) {
                                if (offers.hasOwnProperty(key5)) {
                                    var q_forward = q_forward + offers[key5].unitsCleared;
                                    price_forward.push(offers[key5].priceCleared)
                                }
                            }
                        }
                        // SPOT - STAGE 2
                        if (phases[key3].idd == 2) {
                            // filter offers made in each phase, that were cleared
                            let offers2 = $.grep(this.props.offers, function (n, i) {
                                return (n.phase == phases[key3].id & n.group == rows[key].group_id & n.cleared == true);
                            })
                            for (var key4 in offers2) {
                                if (offers2.hasOwnProperty(key4)) {
                                    q_spot = q_spot + offers2[key4].unitsCleared;
                                    price_spot.push(offers2[key4].priceCleared)

                                }
                            }
                        }
                    }
                }

                // save to ROWS object
                rows[key].price_spot = String(Math.round(average(price_spot))) + "/" + String((getMedian(price_spot) * 100) / 100);
                rows[key].price_forward = String(Math.round(average(price_forward))) + "/" + String((getMedian(price_forward) * 100) / 100);
                rows[key].price_expspot = Math.round(this.props.treatment.price_avg_theory);
                rows[key].row_id = String(rows[key].group_id) + String(rows[key].period_id);
            }
        }
        var Map_table = rows.map(function (r) {
            return ( <Table_row
                key={r.row_id}
                period_id={r.period_idd}
                group_id={r.group_idd}
                demand={r.demand}
                price_forward={r.price_forward}
                q_forward={r.q_forward}
                price_spot={r.price_spot}
                q_spot={r.q_spot}
                profit={r.profit}
            > </Table_row>);

        });

        var Table_head = <tr>
            <th scope="col">R</th>
            <th scope="col">Gr</th>
            <th scope="col">F-P avg/med</th>
            <th scope="col">F-PR/RE pos.</th>
            <th scope="col">Market Qd</th>
            <th scope="col">S-P avg/med</th>
            <th scope="col">S-PR/RE pos.</th>
            <th scope="col">Profits</th>
        </tr>
        return (
            <div>
                <table className="table table-striped table-condensed">
                    <thead> {Table_head} </thead>
                    <tbody>
                    {Map_table}
                    </tbody>
                </table>
            </div>
        )
    }
});

window.Table_main = Table_main;
