// DISTRIB INTERFACE FOR AUCTION EXPERIMENT


// used functions
function mode(array) {
    if (array.length == 0)
        return null;
    var modeMap = {};
    var maxEl = array[0], maxCount = 1;
    for (var i = 0; i < array.length; i++) {
        var el = array[i];
        if (modeMap[el] == null)
            modeMap[el] = 1;
        else
            modeMap[el]++;
        if (modeMap[el] > maxCount) {
            maxEl = el;
            maxCount = modeMap[el];
        }
    }
    return maxEl;
}
function standardDeviation(values) {
    var avg = average(values);
    var squareDiffs = values.map(function (value) {
        var diff = value - avg;
        var sqrDiff = diff * diff;
        return sqrDiff;
    });
    var avgSquareDiff = average(squareDiffs);
    var stdDev = Math.sqrt(avgSquareDiff);
    return stdDev;
}
function average(data) {
    var sum = data.reduce(function (sum, value) {
        return sum + value;
    }, 0);
    var avg = sum / data.length;
    return avg;
}
function roundTen(value) {
    return Math.round(value / 10) * 10
}

function arrayMin(arr) {
    var len = arr.length, min = Infinity;
    while (len--) {
        if (Number(arr[len]) < min) {
            min = Number(arr[len]);
        }
    }
    return min;
};
function arrayMax(arr) {
    var len = arr.length, max = -Infinity;
    while (len--) {
        if (Number(arr[len]) > max) {
            max = Number(arr[len]);
        }
    }
    return max;
};
// master object
var Distrib_master = React.createClass({
    // set init. state to empty
    getInitialState: function () {
        return {
            distr_draws: [],
            auction_f: [],
            my_draw: [],
            draws_demand: [],
            draws_price: [],
            distr_draws_price: [],
            distr_draws_demand: [],
            distr_todraw_demand: [],
            distrib1: [],
            distrib2: [],
            distr_todraw_price: [],
            price_max: [],
            demand_max: [],
            bar_width_q: 1,
            bar_width_p: 1,
            price_mean: [],
            price_std: [],
            demand_mean: [],
            demand_std: [],
            demand_min: [],
            price_min: [],
            test: [],
            distr_draws_l: []
        };
    },

    // get random draws and distrib params, stays the same
    // get my number of random draws
    fetchDrawData: function () {
        $.get("/api/draw/", function (data) {
            window.my_drawsG = data.cur_draw.draw_id;
            if (this.isMounted()) {
                this.setState({
                    my_draw: data.cur_draw.draw_id
                });
            }
        }.bind(this));
    },
    fetchDistribData: function () {
        $.get("/api/distrib/", function (data) {
            if (this.isMounted()) {
                var s_distr_draws = data.distr_draws;
                var distr_draws_l = data.distr_draws.length;
                // split distr draws
                var distr_draws_price = [];
                var distr_draws_demand = [];
                for (var key in s_distr_draws) {
                    if (s_distr_draws.hasOwnProperty(key)) {
                        distr_draws_demand.push((s_distr_draws[key].demand_draw));
                        distr_draws_price.push((s_distr_draws[key].price_draw));
                    }
                }
                var s_auction_f = data.auction_f;
                // make random draw according to para in auctin
                var draws_demand = [];
                var draws_price = [];
                var draws_n = 200000;
                /// q to p transformation
                function q_to_p(q) {
                    var draw_price = (s_auction_f.a * Math.pow((q / s_auction_f.PR_per_group), (s_auction_f.convexity_parameter - 1)));
                    return draw_price
                }
                /// if normal
                if (s_auction_f.distribution_used == 1) {
                    var mu = s_auction_f.mu;
                    var sigma = s_auction_f.sigma;
                    for (var i = 0; i < draws_n; i++) {
                        var draw_demand = (Math.randomGaussian(mu, sigma));
                        if (draw_demand < 0) {
                            var draw_demand = (Math.randomGaussian(mu, sigma));
                        }
                        var draw_price = q_to_p(draw_demand);
                        draws_demand.push(Math.round(draw_demand));
                        draws_price.push(Math.round(draw_price));
                    }
                    /// if uniform
                } else {
                    var u_max= s_auction_f.uniform_max;
                    var u_min = s_auction_f.uniform_min;
                    var region = u_max - u_min
                    // simulate price and quantity draws
                    for (var i = 0; i < draws_n; i++) {
                        var draw_demand = (Math.random() * (u_min - u_max) + u_max);
                        if (draw_demand < 0) {
                            var draw_demand = (Math.random() * (u_min - u_max) + u_max);
                        }
                        var draw_price = q_to_p(draw_demand)
                        draws_demand.push(Math.round(draw_demand * 100)/100);
                        draws_price.push(Math.round(draw_price* 100)/100);
                    }
                      // determine width of the bars based on distribution
                    //console.log("r", region)
                        if (region<=30) {
                            var bar_width_q = 0.1
                            // price is 3.3 of demand
                            var bar_width_p =  0.1
                        } else if  (region<=50)   {
                            var bar_width_q = 0.5
                            // price is 3.3 of demand
                            var bar_width_p =  1
                        } else if  (region<=80)   {
                            var bar_width_q = 1
                            // price is 3.3 of demand
                            var bar_width_p =  5
                        } else {
                            var bar_width_q = 2
                            // price is 3.3 of demand
                            var bar_width_p =  25

                        }


                }
                // initial state for list for plots and tables
                var array1 = [];
                var array2 = [];
                var my_dra = window.my_drawsG;
                var distrib1 = [];
                var distrib2 = [];
                var helper = [];
                for (var key in distr_draws_demand) {
                    if (distr_draws_demand.hasOwnProperty(key)) {
                        if (key < my_dra) {
                            array1.push(distr_draws_demand[key]);
                            array2.push(distr_draws_price[key]);
                            if (key >= (my_dra - 60)) {
                                // if is in second list
                                helper.push(s_distr_draws[key]);
                            }

                        }
                    }
                }
                for (var i in helper) {
                    if (i >= (30)) {
                        distrib2.push(helper[i]);
                    }
                    if (i < 30) {
                        // if is in first list
                        distrib1.push(helper[i]);
                    }
                }
                var price_max = roundTen(arrayMax(draws_price));
                var demand_max = roundTen(arrayMax(draws_demand));
                var price_min = roundTen(arrayMin(draws_price) - 10);
                var demand_min = roundTen(arrayMin(draws_demand) - 10);

                // generate averages and st. devs
                var price_mean = Math.round(average(draws_price));
                var price_std = Math.round(standardDeviation(draws_price));
                if (s_auction_f.distribution_used == 1) {
                    var demand_mean = mu;
                    var demand_std = sigma;
                } else {
                    var demand_mean = Math.round(u_min + (u_max - u_min) / 2);
                    var demand_std = Math.round(Math.sqrt(Math.pow((u_max - u_min), 2) * 1 / 12));
                }
                //(s_auction_f.a* Math.pow((Math.randomGaussian(mu, sigma)/s_auction_f.PR_per_group), (s_auction_f.convexity_parameter-1)));

                this.setState({
                    bar_width_q: bar_width_q,
                    bar_width_p: bar_width_p,
                    distr_draws_l: distr_draws_l,
                    test: my_dra,
                    price_mean: price_mean,
                    price_std: price_std,
                    demand_mean: demand_mean,
                    demand_std: demand_std,
                    distr_draws: s_distr_draws,
                    auction_f: s_auction_f,
                    draws_demand: draws_demand,
                    draws_price: draws_price,
                    distr_draws_price: distr_draws_price,
                    distr_draws_demand: distr_draws_demand,
                    distr_todraw_demand: array1,
                    distr_todraw_price: array2,
                    my_draw: my_dra,
                    distrib1: distrib1,
                    distrib2: distrib2,
                    price_max: price_max,
                    demand_max: demand_max,
                    button_disabled: "active",
                    price_min: price_min,
                    demand_min: demand_min,
                });
            }
        }.bind(this));
    },
    // fetch data on reload immediately, then refresh data in set interval
    componentDidMount: function () {
        this.fetchDrawData();
        setTimeout(function () {
            this.fetchDistribData();
        }.bind(this), 1200);
    },
    handleResetDraws: function () {
        var reset = {new_draw_n: "reset"};
        $.ajax({
            type: "POST",
            url: "/api/draw/",
            data: reset
        });
        this.setState({distr_todraw_demand: [], distr_todraw_price: [], my_draw: 0, distrib1: [], distrib2: []});
    },
    handleNewDraw: function () {
        //console.log("new draw fired!")
        // adds 1 draw to table and plot
        if (this.state.button_disabled == "active") {
            var my_dra = this.state.my_draw + 10;
            var my_dra_ajax = {new_draw_n: my_dra};
            var cur_length = this.state.distr_todraw_demand.length + 10;
            // add element to current state
            var array1 = this.state.distr_todraw_demand.concat(this.state.distr_draws_demand.slice(this.state.my_draw, cur_length));
            var array2 = this.state.distr_todraw_price.concat(this.state.distr_draws_price.slice(this.state.my_draw, cur_length));
            var to_table = this.state.distr_draws.slice(Math.max(cur_length - 60, 0), cur_length);
            var distrib1 = to_table.slice(0, 30);
            var distrib2 = to_table.slice(30, 60);
            setTimeout(function () {
                this.setState({button_disabled: "active"});
            }.bind(this), 200);
            this.setState({
                // cooling down period (now disabled)
                button_disabled: "disabled",
                // to plot
                distr_todraw_demand: array1,
                distr_todraw_price: array2,
                my_draw: my_dra,
                // to table
                distrib1: distrib1,
                distrib2: distrib2
            });

            // performance, will save to server only if number of draws is divisible by 50 without remainder
            if (my_dra == this.state.auction_f.d_draws_needed) {
                var finished = {new_draw_n: "done"};
                $.ajax({
                    type: "POST",
                    url: "/api/draw/",
                    data: finished
                });
            }
            if ((my_dra % 50 === 0) | (my_dra == this.state.auction_f.d_draws_needed)) {
                $.ajax({
                    type: "POST",
                    url: "/api/draw/",
                    data: my_dra_ajax,
                });
            }
            this.forceUpdate()
        }
    },
    handleWidthChange: function (e) {
        this.setState({bar_width: parseInt(e.target.value)});
    },
    render: function () {
        // timestamp for plot
        var timest = Math.round(+new Date() / 1);
        // create vars for buttons
        var draws_needed = this.state.auction_f.d_draws_needed;
        if (draws_needed == null) {
            var draws_needed = 999;
            var Buttons = <div>
                <div className="col-lg-3">
                    <button className={button_dist} onClick={this.handleNewDraw}>Loading.....</button>

                </div>
                <div className="col-lg-3">
                    <h4><b>
                        <p>
                            <center>Make draws and watch how the distribution of your draws (in black) is converging to
                                the given distribution (in red)
                            </center>
                        </p>
                    </b></h4>

                </div>
            </div>;
        } else {
            if (this.state.my_draw < draws_needed) {
                var draws_remaining = draws_needed - this.state.my_draw;
                var button_dist = "btn btn-danger btn-lg " + this.state.button_disabled;
                // if I still need to draw
                var Buttons = <div>
                    <div className="col-lg-3">
                        <button className={button_dist} onClick={this.handleNewDraw}>CLICK HERE to
                            make {draws_remaining} more draws
                        </button>
                    </div>
                    <div className="col-lg-3">
                        <h4><b>
                            <p>
                                <center>Make draws and watch how the distribution of your draws (in black) is
                                    converging to the given distribution (in red)
                                </center>
                            </p>
                        </b></h4>
                    </div>
                </div>;
            } else {
                if (this.state.my_draw == this.state.distr_draws_l) {
                    var button_dist_completed = "btn disabled btn-lg " + this.state.button_disabled;
                    var Buttons = <div>
                        <div className="col-lg-3">
                            <button className={button_dist_completed}><p>You have drawn the maximum available number of
                                draws.
                            </p></button>
                        </div>
                        <div className="col-lg-9">
                            <h4>Wait until experiment continues....</h4>
                        </div>
                    </div>;
                } else {
                    var button_dist_completed = "btn btn-success btn-lg " + this.state.button_disabled;
                    var Buttons = <div>
                        <div className="col-lg-3">

                            <button className={button_dist_completed} onClick={this.handleNewDraw}>CLICK HERE to draw
                                more
                                draws
                            </button>
                        </div>
                        <div className="col-lg-9">
                            <h4>Wait until experiment continues....</h4>
                        </div>
                    </div>;
                }
            }
        }
        return (
            <div className="container-fluid">
                <div className="row">               {/*<!-- ROW 1 -->*/}
                    <div className="col-lg-5">           {/*<!-- ROW 1, COLUMN 1 -->*/}
                        <h2 className="text-center">RANDOM DRAWS </h2>
                    </div>
                           <div className="col-lg-2" style={{fontSize: "150%"}} id="Timer"></div>
                    <div className="col-lg-5">           {/*<!-- ROW 1, COLUMN 2 -->*/}
                        <h2 className="text-center"><br/>GRAPHICAL DISPLAYS</h2>
                    </div>
                </div>
                <div className="row">                {/*<!-- ROW 2 -->*/}
                    <Distrib_table distrib1={this.state.distrib1} distrib2={this.state.distrib2} timestamp={timest}/>
                    <div className="col-lg-6">         {/*  <!-- ROW 2, COLUMN 3 -->*/}
                        <div className="row">          {/* <!-- ROW 2, COLUMN 3, ROW 1 -->*/}
                            <Dist_plot1 bar_width_q={this.state.bar_width_q}
                                        data1={this.state.draws_demand}
                                        data2={this.state.distr_todraw_demand}
                                        timestamp={timest}
                                        demand_mean={this.state.demand_mean}
                                        demand_max={this.state.demand_max}
                                        demand_min={this.state.demand_min}
                            />
                            <div style={{float: "left"}}>Average: {this.state.demand_mean} --- Standard
                                Deviation: {this.state.demand_std}.
                            </div>
                        </div>
                        <div className="row">            {/*<!-- ROW 2, COLUMN 3, ROW 2 -->*/}
                            <Dist_plot2 bar_width_p={this.state.bar_width_p}
                                        data1={this.state.draws_price}
                                        data2={this.state.distr_todraw_price}
                                        timestamp={timest}
                                        price_mean={this.state.price_mean}
                                        price_max={this.state.price_max}
                                        price_min={this.state.price_min}
                            />
                            <div style={{float: "left"}}>Average: {this.state.price_mean} --- Standard
                                Deviation: {this.state.price_std}.
                            </div>
                        </div>
                    </div>
                </div>
                <div className="row">               {/* <!-- ROW 3 -->*/}

                    {Buttons}
                </div>

            </div>
        )
    }
});
ReactDOM.render(<Distrib_master/>, document.getElementById("Distrib_app"));

