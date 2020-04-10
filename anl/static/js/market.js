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
            Plotly.plot(handle, data, layout, {staticPlot: false, displayModeBar: false}));
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
                    if (sorted_offers_id[key].cleared == "true" && sorted_offers_id[key].offer_tiepe == 1 && sorted_offers_id[key].canceled == "false") {
                        transactions_price.push(sorted_offers_id[key].priceCleared);
                        transactions_units.push(sorted_offers_id[key].unitsCleared);
                        demandR_price.push(sorted_offers_id[key].priceOriginal);
                        demandR_units.push(sorted_offers_id[key].unitsCleared);
                    }
                    if (sorted_offers_id[key].cleared == "true" && sorted_offers_id[key].offer_tiepe == 0 && sorted_offers_id[key].canceled == "false") {
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
                    if (sorted_offers[key].cleared == "false" && sorted_offers[key].canceled == "false") {
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
            }
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
                width: 5,
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
                width: 1,
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
                width: 1,
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
            autosize: "False",
            width: this.props.plot_w,
            height: this.props.plot_l,

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

// main element
var Market = React.createClass({
    getInitialState: function () {
        // initialized to N/A for display
        return {
            offers: [],
            periods: [],
            phases: [],
            cur_period: {idd: 'N/A', total_demand: 'N/A', dura: "N/A"},
            cur_phases: [],
            cur_phase: {idd: 'N/A', dura: "N/A"},
            cur_offers: [],
            d_offers: [],
            map_phases: [],
            time: "N/A",
            per_selected: 0,
            phase_selected: 0,
            speed: 1000,
            play_indic: "",
            data_msg: "",
            data_live: 0,
            auction: ""

        };
    },

    // fetch csv data from staticfiles
    fetchData: function () {
// //         if (variable == null){
// //     // your code here.
//         function isEmpty(obj) {
//             return (Object.getOwnPropertyNames(obj).length);
//         }
//
//         console.log(window.cur_offers)
//         if (window.cur_auction == "[]" || window.cur_periods == "[]" || window.cur_offers == "[]" || window.cur_phases == "[]") {
//             var missing = ""
//             if (window.cur_auction == "[]") {
//                 var missing = missing + " auction"
//             }
//             if (window.cur_periods == "[]") {
//                 var missing = missing + " periods"
//             }
//             if (window.cur_offers == "[]") {
//                 var missing = missing + " offers"
//             }
//             if (window.cur_phases == "[]") {
//                 var missing = missing + " phases"
//             }
//             this.setState({
//                 data_msg: "Live data from DB import failed, missing" + missing,
//             });
            this.fetchVSEPilot()
        // } else {
        //
        //     console.log(window.cur_offers == "[]")
        //     var parse_auct = window.cur_auction.replace(/\'/g, '\"').replace(/\False/g, '0').replace(/\True/g, '1').replace(/\None/g, '');
        //     var parse_offers = window.cur_offers.replace(/\'/g, '\"').replace(/\False/g, '0').replace(/\True/g, '1').replace(/\None/g, '');
        //     var parse_phases = window.cur_phases.replace(/\'/g, '\"').replace(/\False/g, '0').replace(/\True/g, '1').replace(/\None/g, '');
        //     var parse_periods = window.cur_periods.replace(/\'/g, '\"').replace(/\False/g, '0').replace(/\True/g, '1').replace(/\None/g, '');
        //     this.setState({
        //         // data_msg: "Importing data from DB",
        //         //     offers: window.cur_offers,
        //         //     periods: window.cur_periods,
        //         //     phases: window.cur_phases,
        //         data_live: 1,
        //         data_msg: "Data from DB parsed.",
        //         auction: JSON.parse(parse_auct),
        //         offers: JSON.parse(parse_offers),
        //         periods: JSON.parse(parse_periods),
        //         phases: JSON.parse(parse_phases)
        //     });
        // }

    },
    fetchVSEPilot: function () {
        $.ajax({
            url: "/staticfiles/data/dauction2_public_dAuction2_offer.csv",
            success: function (csvd) {
                var data = $.csv.toObjects(csvd);
                this.setState({
                    offers: data,
                });
            }.bind(this)
        });
        $.ajax({
            url: "/staticfiles/data/dauction2_public_dAuction2_period.csv",
            success: function (csvd) {
                var data = $.csv.toObjects(csvd);
                this.setState({
                    periods: data,
                });
            }.bind(this)
        });
        $.ajax({
            url: "/staticfiles/data/dauction2_public_dAuction2_phase.csv",
            success: function (csvd) {
                var data = $.csv.toObjects(csvd);
                this.setState({
                    phases: data,
                });
            }.bind(this)
        });
    },
    filterData: function () {
        // filter possibility of incomplete data, to prevent mistakes
        // check if every period has its phases, delete incomplete ones
        var periods = this.state.periods;
        var offers = this.state.offers;
        var phases = this.state.phases;
        var new_periods = [];
        var new_phases = [];
        for (var key in periods) {
            if (periods.hasOwnProperty(key)) {
                var per_phases = $.grep(phases, function (n, i) {
                    return n.period_id == periods[key].id;
                });
                if (per_phases.length != 0 & per_phases.length > 1) {
                    new_periods.push(periods[key])
                    new_phases.push(per_phases[0])
                    new_phases.push(per_phases[1])
                }
            }
        }
        // make sure, that atributes of offers are correct
        for (var key in offers) {
            if (offers.hasOwnProperty(key)) {
                if (offers[key].canceled == 0) {
                    offers[key].canceled = "false"
                }
                if (offers[key].canceled == 1) {
                    offers[key].canceled = "true"
                }
                if (offers[key].cleared == 0) {
                    offers[key].cleared = "false"
                }
                if (offers[key].cleared == 1) {
                    offers[key].cleared = "true"
                }
            }
        }
        if (new_phases.length == 0) {
             this.setState({
                data_msg: this.state.data_msg + " But no period and phase survived filtering! There are not two periods corresponding to first phase in the data."
            });
        }
        this.setState({
            //offers: JSON.parse(parse_offers),
            periods: new_periods,
            phases: new_phases,
            offers: offers
        });

    },
    // destring all time data, and make them relative to respective period/phase of the period
    // compute duration of periods/phase, time of clearing/creation of offer in respective period/phase
    relativeTime: function () {
        // make shortcuts to data from react
        var periods = this.state.periods;
        var offers = this.state.offers;
        var phases = this.state.phases;
        var new_phases = [];
        // loop for every period
        for (var key in periods) {
            if (periods.hasOwnProperty(key)) {
                console.log(periods[key])
                // destring date of update, and save it as a date of end
                var date_string = periods[key].updated.replace('+00:00', '');
                var split_space = date_string.split(" ")
                var split_date = split_space[0].split("-")
                var split_time = split_space[1].split(":")
                periods[key].end = new Date(split_date[0], split_date[1], split_date[2], split_time[0], split_time[1], split_time[2]);
                // select phases for looped period
                var per_phases = $.grep(phases, function (n, i) {
                    return n.period_id == periods[key].id;
                });
                console.log(per_phases)
                // sort them
                per_phases.sort(sort_by("idd", false, parseInt));
                // should be only 2, select the first one and make it the start of period
                var date_string = per_phases[0].created.replace('+00:00', '');
                var split_space = date_string.split(" ")
                var split_date = split_space[0].split("-")
                var split_time = split_space[1].split(":")
                periods[key].start = new Date(split_date[0], split_date[1], split_date[2], split_time[0], split_time[1], split_time[2]);
                per_phases[0].start = new Date(split_date[0], split_date[1], split_date[2], split_time[0], split_time[1], split_time[2]);
                periods[key].dura = (periods[key].end - periods[key].start) / 1000
                var date_string = per_phases[1].created.replace('+00:00', '');
                var split_space = date_string.split(" ")
                var split_date = split_space[0].split("-")
                var split_time = split_space[1].split(":")
                per_phases[1].start = new Date(split_date[0], split_date[1], split_date[2], split_time[0], split_time[1], split_time[2]);
                per_phases[0].end = new Date(split_date[0], split_date[1], split_date[2], split_time[0], split_time[1], split_time[2]);
                per_phases[0].dura = (per_phases[0].end - periods[key].start) / 1000
                per_phases[1].end = periods[key].end;
                per_phases[1].dura = (periods[key].end - new Date(split_date[0], split_date[1], split_date[2], split_time[0], split_time[1], split_time[2])) / 1000;
                // offers
                /// period
                var period_offers = $.grep(offers, function (n, i) {
                    return (n.phase_id == per_phases[0].id || n.phase_id == per_phases[1].id);
                });
                for (var k in period_offers) {
                    if (period_offers.hasOwnProperty(k)) {
                        if (period_offers[k].timeCleared != "") {
                            var date_string = period_offers[k].timeCleared.replace('+00:00', '')
                            var split_space = date_string.split(" ")
                            var split_date = split_space[0].split("-")
                            var split_time = split_space[1].split(":")
                            period_offers[k].per_clear = (new Date(split_date[0], split_date[1], split_date[2], split_time[0], split_time[1], split_time[2]) - periods[key].start) / 1000;
                        } else {
                            period_offers[k].per_clear = ""
                        }
                        var date_string = period_offers[k].created.replace('+00:00', '')
                        var split_space = date_string.split(" ")
                        var split_date = split_space[0].split("-")
                        var split_time = split_space[1].split(":")
                        period_offers[k].per_created = (new Date(split_date[0], split_date[1], split_date[2], split_time[0], split_time[1], split_time[2]) - periods[key].start ) / 1000;
                        if (period_offers[k].phase_id == per_phases[0].id) {
                            if (period_offers[k].timeCleared != "") {
                                var date_string = period_offers[k].timeCleared.replace('+00:00', '')
                                var split_space = date_string.split(" ")
                                var split_date = split_space[0].split("-")
                                var split_time = split_space[1].split(":")
                                period_offers[k].pha_clear = (new Date(split_date[0], split_date[1], split_date[2], split_time[0], split_time[1], split_time[2]) - per_phases[0].start ) / 1000;
                            } else {
                                period_offers[k].pha_clear = ""
                            }
                            var date_string = period_offers[k].created.replace('+00:00', '')
                            var split_space = date_string.split(" ")
                            var split_date = split_space[0].split("-")
                            var split_time = split_space[1].split(":")
                            period_offers[k].pha_created = (new Date(split_date[0], split_date[1], split_date[2], split_time[0], split_time[1], split_time[2]) - per_phases[0].start) / 1000;
                        }

                        if (period_offers[k].phase_id == per_phases[1].id) {
                            if (period_offers[k].timeCleared != "") {
                                var date_string = period_offers[k].timeCleared.replace('+00:00', '')
                                var split_space = date_string.split(" ")
                                var split_date = split_space[0].split("-")
                                var split_time = split_space[1].split(":")
                                period_offers[k].pha_clear = (new Date(split_date[0], split_date[1], split_date[2], split_time[0], split_time[1], split_time[2]) - per_phases[1].start ) / 1000;
                            } else {
                                period_offers[k].pha_clear = ""
                            }
                            var date_string = period_offers[k].created.replace('+00:00', '')
                            var split_space = date_string.split(" ")
                            var split_date = split_space[0].split("-")
                            var split_time = split_space[1].split(":")
                            period_offers[k].pha_created = (new Date(split_date[0], split_date[1], split_date[2], split_time[0], split_time[1], split_time[2]) - per_phases[1].start) / 1000;
                        }
                    }
                }
                // phased to new element
                new_phases.push(per_phases[0]);
                new_phases.push(per_phases[1]);

            }
        }
        // update state
        this.setState({
            periods: periods,
            phases: new_phases,
            offers: offers
        });

    },
    // function serving period selection buttons
    periodSelect: function (e) {
        var cur_period = $.grep(this.state.periods, function (n, i) {
            return n.id == e.target.value;
        });
        // after period is selected, generate buttons for phase seleciton
        var cur_phases = $.grep(this.state.phases, function (n, i) {
            return n.period_id == e.target.value;
        });
        for (var key in cur_phases) {
            if (cur_phases.hasOwnProperty(key)) {
                cur_phases[key].className = "btn warning";
                cur_phases[key].onClick = this.phaseSelect;
                cur_phases[key].display = cur_phases[key].idd
            }
        }
        cur_phases.push({
            id: "1+2",
            className: "btn warning",
            onClick: this.phaseSelect,
            display: "all phases in period together"
        });
        var Map_phases = cur_phases.map(function (e) {
            return ( <Button
                key={e.idd}
                value={e.id}
                display={e.display}
                function={e.onClick}
                className={e.className}
            >
            </Button>)
        })
        // extract offers present in both phases of respective period
        var phase_id_1 = cur_phases[0].id;
        var phase_id_2 = cur_phases[1].id;
        var cur_offers = $.grep(this.state.offers, function (n, i) {
            return (n.phase_id == phase_id_1 || n.phase_id == phase_id_2);
        });
        var offers_copy = JSON.parse(JSON.stringify(cur_offers));
        for (var key in offers_copy) {
            if (offers_copy.hasOwnProperty(key)) {
                offers_copy[key].priceOriginal = parseInt(offers_copy[key].priceOriginal)
                offers_copy[key].priceCleared = parseInt(offers_copy[key].priceCleared)
                offers_copy[key].offer_tiepe = parseInt(offers_copy[key].offer_tiepe)
                offers_copy[key].unitsCleared = parseInt(offers_copy[key].unitsCleared)
                offers_copy[key].id = parseInt(offers_copy[key].id)
                offers_copy[key].unitsAvailable = parseInt(offers_copy[key].unitsAvailable)
            }
        }
        this.setState({
            cur_period: cur_period[0],
            cur_phases: cur_phases,
            map_phases: Map_phases,
            cur_offers: offers_copy,
            cur_phase: {idd: '1+2', dura: this.state.cur_period.dura},
            d_offers: offers_copy,
            time: cur_period[0].dura,
            per_selected: 1

        });
        // enable slider
        $("#slider").prop('disabled', false);
        $("#slider").prop('max', cur_period[0].dura);
        $("#slider").prop('value', cur_period[0].dura);
        // enable buttons
        $("#play_btn").removeClass("disabled");
        $("#stop_btn").removeClass("disabled");
        $("#play_start_btn").removeClass("disabled");
        this.btnStop()
    },
    // function for selecting phases, added 1+2 value for selection of all offers in period
    phaseSelect: function (e) {
        // if not selection all offers in period
        if (e.target.value != "1+2") {
            var cur_phase = $.grep(this.state.phases, function (n, i) {
                return n.id == e.target.value;
            });
            var cur_offers = $.grep(this.state.offers, function (n, i) {
                return n.phase_id == e.target.value;
            });
            var offers_copy = JSON.parse(JSON.stringify(cur_offers));
            for (var key in offers_copy) {
                if (offers_copy.hasOwnProperty(key)) {
                    offers_copy[key].priceOriginal = parseInt(offers_copy[key].priceOriginal)
                    offers_copy[key].priceCleared = parseInt(offers_copy[key].priceCleared)
                    offers_copy[key].offer_tiepe = parseInt(offers_copy[key].offer_tiepe)
                    offers_copy[key].unitsCleared = parseInt(offers_copy[key].unitsCleared)
                    offers_copy[key].id = parseInt(offers_copy[key].id)
                    offers_copy[key].unitsAvailable = parseInt(offers_copy[key].unitsAvailable)
                }
            }
            this.setState({
                cur_phase: cur_phase[0],
                cur_offers: offers_copy,
                d_offers: offers_copy,
                time: cur_phase[0].dura,
                phase_selected: 1

            });
            // slider
            $("#slider").prop('max', cur_phase[0].dura);
            $("#slider").prop('value', cur_phase[0].dura);
            this.btnStop()
            // if selecting all offers in both phases
        } else {
            var period_id = this.state.cur_period.id
            var cur_phases = $.grep(this.state.phases, function (n, i) {
                return n.period_id == period_id
            });
            var phase_id_1 = cur_phases[0].id;
            var phase_id_2 = cur_phases[1].id;
            var cur_offers = $.grep(this.state.offers, function (n, i) {
                return (n.phase_id == phase_id_1 || n.phase_id == phase_id_2);
            });
            var offers_copy = JSON.parse(JSON.stringify(cur_offers));
            for (var key in offers_copy) {
                if (offers_copy.hasOwnProperty(key)) {
                    offers_copy[key].priceOriginal = parseInt(offers_copy[key].priceOriginal)
                    offers_copy[key].priceCleared = parseInt(offers_copy[key].priceCleared)
                    offers_copy[key].offer_tiepe = parseInt(offers_copy[key].offer_tiepe)
                    offers_copy[key].unitsCleared = parseInt(offers_copy[key].unitsCleared)
                    offers_copy[key].id = parseInt(offers_copy[key].id)
                    offers_copy[key].unitsAvailable = parseInt(offers_copy[key].unitsAvailable)
                }
            }
            this.setState({
                cur_phase: {idd: '1+2', dura: this.state.cur_period.dura},
                cur_offers: offers_copy,
                d_offers: offers_copy,
                time: this.state.cur_period.dura,
                phase_selected: 0
            });
            // slider
            $("#slider").prop('max', this.state.cur_period.dura);
            $("#slider").prop('value', this.state.cur_period.dura);
            this.btnStop()
        }
    },
    // function of change of slider value
    slider_change: function (e) {
        this.setState({
            d_offers: []
        });

        var slider_time = e.target.value
        // filter offers
        var offers = JSON.parse(JSON.stringify(this.state.cur_offers));
        var new_offers = []
        // filter offers, if offer is created in time period and if its cleared after time period, change to ontcleared
        for (var key in offers) {
            if (offers.hasOwnProperty(key)) {
                // for period or 1+2 phases
                if (this.state.cur_phase.idd == "1+2") {
                    if (slider_time >= offers[key].per_created) {
                        if (slider_time < offers[key].per_clear) {
                            offers[key].cleared = "false"
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
                            offers[key].cleared = "false"
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
            d_offers: new_offers
        });
    },
    // function for the play button
    btnPlay: function (e) {
        if (window.checker == false && this.state.cur_period.idd != "N/A") {
            if (e.target.value == "normal") {
                if ((this.state.phase_selected == 0 && this.state.time != this.state.cur_period.dura) || (this.state.phase_selected == 1 && this.state.time < this.state.cur_phase.dura)) {

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
    innerPlay: function() {
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
            speed: 1000,
            play_indic: ""
        })
    },
    // execute when all its loaded, only once
    componentWillMount: function () {
        this.fetchData();
        setTimeout(function () {
            this.filterData()
            setTimeout(function () {
                this.relativeTime();
            }.bind(this), 100);
        }.bind(this), 500);
        window.checker = false
    },
    componentDidMount: function () {
    },
    refetchVSEdata: function () {
        this.fetchVSEPilot();
        setTimeout(function () {
            this.filterData()
            setTimeout(function () {
                this.relativeTime();
            }.bind(this), 100);
        }.bind(this), 500);
        window.checker = false
        this.btnReset()
        this.setState({
            data_msg: "",
            data_live: 0
        });
    },

    render () {
        // render initial period buttons
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
        var time_slider = String(this.state.time)
        var plot_w = $(window).width() * 0.6;
        var plot_h = $(window).height() * 0.6;
        // timestamp for plot (otherwise will not refresh)
        var timest = new Date().getTime();
        console.log(timest)
        // phase and period select indicator
        if (this.state.per_selected == 0) {
            var per_text = <div className="alert-danger container"><b> SELECT PERIOD </b></div>
        } else {
            var per_text = <div><b>PERIOD:</b> {this.state.cur_period.idd} Total
                Demand: {this.state.cur_period.total_demand} Duration: {this.state.cur_period.dura}</div>
        }
        if (this.state.phase_selected == 0 && this.state.per_selected == 0) {
            var phase_text = <div></div>
        } else if (this.state.phase_selected == 0 && this.state.per_selected == 1) {
            var phase_text = <div className="alert-warning">Data for all phases in period loaded, select phase bellow
                for separation</div>
        } else {
            var phase_text = <div><b>PHASE:</b> {this.state.cur_phase.idd} Duration: {this.state.cur_phase.dura}</div>
        }
        // check if finished
        if ((this.state.time == this.state.cur_period.dura) || (this.state.phase_selected == 1 && this.state.time == this.state.cur_phase.dura)) {
            console.log("fire!")
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
        if (this.state.data_live == 0) {
            var data_info = "Loaded data from VSE pilot in May (csv import)"
            var data_button = <div></div>
        } else {
            var data_info = "Loaded live data from auction created at " + this.state.auction.created
            var data_button = <div>
                <button
                    id="play_btn"
                    onClick={this.refetchVSEdata}
                    className="btn btn-primary"
                    value="plus"

                >
                    Load data from VSE pilot
                </button>
            </div>
        }
        return (
            <div className="row container-fluid">
                <div id="plot" className="row container-fluid">
                    <div className="col-lg-12">
                        <MarketPlot all_offers={this.state.d_offers} plot_w={plot_w} plot_l={plot_h}
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
                            <div className="btn-group btn-default">
                                {this.state.map_phases}
                            </div>
                        </div>
                        <div id="data_text">
                            <div><b>Loaded data info:</b></div>
                            <div>{this.state.data_msg}</div>
                            <div>{data_info}</div>
                            <div>{data_button}</div>
                        </div>
                    </div>

                </div>
            </div>
        )
    }
});

// render to div id="cost_tables"
ReactDOM.render(<Market/>, document.getElementById("market"));

