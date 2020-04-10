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
// Plot rendering, same as main auction
var RP = React.createClass({
    propTypes: {
        handle: React.PropTypes.string.isRequired,
        data: React.PropTypes.array.isRequired,
        layout: React.PropTypes.object
    },
    componentDidMount: function componentDidMount() {
        this.plot(this.props);
    },
    componentWillReceiveProps: function (nextProps) {
        this.plot(nextProps);
    },
    plot: function plot(props) {
        var handle = props.handle,
            data = props.data,
            layout = props.layout;
        return (
            Plotly.plot(handle, data, layout));
    },
    render() {
        return React.createElement('divfghgfh', {id: this.props.handle}, "");
    }
});
var MarketPlot = React.createClass({
    render () {
        // if incoming object is empty
        if (this.props.all_offers.length == 0) {
            // empty vars to plot
            var demand_price = [], demand_units = [], supply_price = [], supply_units = [];
            var demandR_price = [], demandR_units = [], supplyR_price = [], supplyR_units = [];
            // if nonempty, calculate
        } else {
            // calculate graph data from data about all offers
            // destring needed vars
            // offer_tiepe, priceOriginal, priceCleared, unitsCleared, unitsAvailiable. unitsAvailable
            var offers_copy = JSON.parse(JSON.stringify(this.props.all_offers));
            // all cleared offers, sorted by id
            var offers_copy1 = JSON.parse(JSON.stringify(offers_copy));
            var sorted_offers_id = offers_copy1.sort(sort_by("id", false, parseInt));
            // predefine arrays
            var transactions_price = [], transactions_units = [];
            var demandR_price = [], demandR_units = [], supplyR_price = [], supplyR_units = [];
            // extract elements
            for (var key in sorted_offers_id) {
                if (sorted_offers_id.hasOwnProperty(key)) {
                    if (sorted_offers_id[key].cleared == true && sorted_offers_id[key].offer_tiepe == 1) {
                        transactions_price.push(sorted_offers_id[key].priceCleared);
                        transactions_units.push(sorted_offers_id[key].unitsCleared);
                        demandR_price.push(sorted_offers_id[key].priceOriginal);
                        demandR_units.push(sorted_offers_id[key].unitsCleared);
                    }
                    if (sorted_offers_id[key].cleared == true && sorted_offers_id[key].offer_tiepe == 0) {
                        supplyR_price.push(sorted_offers_id[key].priceOriginal);
                        supplyR_units.push(sorted_offers_id[key].unitsCleared);
                    }

                }
            }
            ;
            // all cleared offers, ordered by price
            var offers_copy2 = JSON.parse(JSON.stringify(offers_copy));
            var sorted_offers = offers_copy2.sort(sort_by("priceOriginal", true, parseInt));
            // predefine arrays
            var demand_price = [], demand_units = [], supply_price = [], supply_units = [];
            // loop offer object to create diff variables
            for (var key in sorted_offers) {
                if (sorted_offers.hasOwnProperty(key)) {
                    // if not cleared
                    if (sorted_offers[key].cleared == false && sorted_offers[key].canceled == false) {
                        if (sorted_offers[key].offer_tiepe == 1) {
                            //sell_listSTx.push(sorted_offers[key]);
                            demand_price.push(sorted_offers[key].priceOriginal);
                            demand_units.push(sorted_offers[key].unitsAvailable);
                        } else {
                            //buy_listSTx.unshift(0,elt)
                            supply_price.unshift(sorted_offers[key].priceOriginal);
                            supply_units.unshift(sorted_offers[key].unitsAvailable);
                        }

                    }
                }
            }
            // sum all quantities
            var demand_unitsS = [], demandR_unitsS = [], supply_unitsS = [], supplyR_unitsS = [],
                transactions_unitsS = [];
            demand_units.reduce(function (a, b, i) {
                return demand_unitsS[i] = a + b;
            }, 0);
            demandR_units.reduce(function (a, b, i) {
                return demandR_unitsS[i] = a + b;
            }, 0);
            supply_units.reduce(function (a, b, i) {
                return supply_unitsS[i] = a + b;
            }, 0);
            supplyR_units.reduce(function (a, b, i) {
                return supplyR_unitsS[i] = a + b;
            }, 0);
            transactions_units.reduce(function (a, b, i) {
                return transactions_unitsS[i] = a + b;
            }, 0);
            //console.log(demand_unitsS, demandR_unitsS, supply_unitsS, supplyR_unitsS)
            // doubley/doublex to plot
            function doubleY(array) {
                if (array.length > 0) {
                    return array.map(function (e, i) {
                        return [e, array[i]];
                    }).reduce(function (a, b) {
                        return a.concat(b);
                    }, []);
                } else {
                    return [0]
                }
            }

            function doubleX(array) {
                if (array.length > 0) {
                    let result = array.map(function (e, i) {
                        return [e, array[i]];
                    }).reduce(function (a, b) {
                        return a.concat(b);
                    }, []);
                    // add zero at the front, remove last value
                    result.unshift(0);
                    result.pop();
                    return result
                } else {
                    return [0]
                }
            }

            // apply doubleX to  quantities
            var demand_unitsSP = doubleX(demand_unitsS), demandR_unitsSP = doubleX(demandR_unitsS),
                supply_unitsSP = doubleX(supply_unitsS), supplyR_unitsSP = doubleX(supplyR_unitsS),
                transactions_unitsSP = doubleX(transactions_unitsS);
            // doubleY to prices
            var demand_priceP = doubleY(demand_price), supply_priceP = doubleY(supply_price),
                demandR_priceP = doubleY(demandR_price), supplyR_priceP = doubleY(supplyR_price),
                transactions_priceP = doubleY(transactions_price);
            // cleared function must push the noncleared one to the right
            var demand_unitsSP = demand_unitsSP.map(function (e, i) {
                return demand_unitsSP[i] + transactions_unitsSP[transactions_unitsSP.length - 1]
            });
            var supply_unitsSP = supply_unitsSP.map(function (e, i) {
                return supply_unitsSP[i] + transactions_unitsSP[transactions_unitsSP.length - 1]
            });
        }
        // main supply
        var trace2 = {
            x: supply_unitsSP,
            y: supply_priceP,
            name: 'supply',
            type: 'scatter',
            mode: 'lines',
            line: {
                color: 'orange',
                width:7,
            }
        };
        // main demand
        var trace1 = {
            x: demand_unitsSP,
            y: demand_priceP,
            name: 'demand',
            mode: 'lines',
            type: 'scatter',
            line: {
                color: 'blue',
width:7,            }
        };
        // coordinates for transactions
        var trace3 = {
            x: transactions_unitsSP,
            y: transactions_priceP,
            name: 'transactions',
            mode: 'lines',
            type: 'scatter',
            line: {
                color: 'black',
                width: 3,
                dash: 1
            }
        };
        // supply for offers that went to transaction
        var trace5 = {
            x: supplyR_unitsSP,
            y: supplyR_priceP,
            name: 'realised supply',
            mode: 'lines',
            type: 'scatter',
            line: {
                color: 'orange',
                width: 3,
                dash: 3
            }
        };
        // demand for offers that went to transaction
        var trace4 = {
            x: demandR_unitsSP,
            y: demandR_priceP,
            name: 'realised demand',
            mode: 'lines',
            type: 'scatter',
            line: {
                color: 'blue',
                width: 3,
                dash: 3
            }
        };
        var layout = {
            margin: {
                r: 25,
                b: 25,
                l: 25,
                t: 25
            },
            // autosize: "False",
            // width: this.props.plot_w,
            // height: this.props.plot_l,

        };
        var data1 = [trace1, trace2, trace3, trace4, trace5];
        return (
            <div id="testeeeee"
            >
                <RP id="myDivee"

                    handle="myDiertev" data={data1} layout={layout} ref="refee" key={this.props.timestamp}/>
            </div>
        );
    }
});

window.MarketPlot = MarketPlot;
