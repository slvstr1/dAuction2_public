/**
 * Created by marce on 29-Apr-17.
 */
// page 14 in the full instructions
/// Elaborate example for Marcel

// we want to generate two tables with first 10 vouchers for the producer and place them side by side
// one has no used vouchers, the other has 7 used vouchers
// we will use voucher object to have a dynamic costs based on current setting of the experiment
// Im not able to use only JS, maybe you are, here is simple example in React


// define row of the table as an object, we will use it to generate rows using map function
var TableRow = React.createClass({
    render: function () {
        return (<tr>
                <td style={{textAlign: "center"}}>{this.props.idd}</td>
                <td>{this.props.value}</td>
                <td>{this.props.usedV}</td>
            </tr>
        )
    }
});

// define the main table object
var Tables = React.createClass({
    render: function () {
        // ***  THIS PART OF THE CODE WILL BE REUSED IN OTHER CASES TO GET DATA FROM WEBPAGE TO JS
        // get data from divs, replace '' with "", True with 1 and False with 0, shoud be present in every file
        var treatment_d = (($('#treatment_js').text()).replace(/\'/g, '\"')).replace(/\False/g, '0').replace(/\True/g, '1');
        var vouchers_d = (($('#vouchers_js').text()).replace(/\'/g, '\"')).replace(/\False/g, '0').replace(/\True/g, '1');
        // whats is the treatment:
        // {'mu': 60.0, 'convexity_parameter': 4, 'uniform_min': 20, 'short_maximum': 15, 'penalty_perunit': 10,
        // 'treatment_started': False, 'app': 1, 'a': 0.017777777777, 'retail_price': 197.0, 'PR_per_group': 4,
        // 'd_draws_needed': 400, 'sigma': 20.0, 'time_conditional': 20, 'end': False, 'show_ids': False,
        // 'uniform_max': 100, 'time_refresh_data': 2000, 'max_vouchers': 35}
        var treatment = $.parseJSON(treatment_d);
        // whats in vouchers:
        // [{'id': 1, 'idd': 1, 'value': 0.0, 'treatment_id': 1}, {'id': 2, 'idd': 2, 'value': 0.0, 'treatment_id': 1},
        // {'id': 3, 'idd': 3, 'value': 0.1, 'treatment_id': 1}, {'id': 4, 'idd': 4, 'value': 0.3, 'treatment_id': 1},
        // {'id': 5, 'idd': 5, 'value': 0.7, 'treatment_id': 1}, {'id': 6, 'idd': 6, 'value': 1.7, 'treatment_id': 1},
        // ...] array of voucher objects, value is cost for the Producer, value for the retailer is treatment.retail_price
        var vouchers = $.parseJSON(vouchers_d);
        var value = treatment.retail_price;
        /// initialize empty array
        var g_vouchers = [];
        /// create 10 vouchers via loop, we need id to use it as a key in react and idd to display voucher # in table
        for (var i = 0; i < 10; i++) {
            g_vouchers.push({'id': i + 1, 'idd': i + 1, "value": value})
        }
        /// copy to two arrays, used in table
        var vouchers_t1 = JSON.parse(JSON.stringify(g_vouchers));
        var vouchers_t2 = JSON.parse(JSON.stringify(g_vouchers));
        // ***


        //add X to vouchers_t1

        for (var key in vouchers_t1) {
            if (vouchers_t1.hasOwnProperty(key)) {
                vouchers_t1[key].usedV = "";
                if (vouchers_t1[key].idd <= 5) {
                    vouchers_t1[key].usedV = "X";
                }
            }
        }
        // add X to vouchers_t2
        for (var key in vouchers_t2) {
            if (vouchers_t2.hasOwnProperty(key)) {
                vouchers_t2[key].usedV = "";
                if (vouchers_t2[key].idd <= -3) {
                    vouchers_t2[key].usedV = "X";
                }
            }
        }
        // map to tables using row object
        var tableMap1 = vouchers_t1.map(function (i) {
            return (<TableRow key={i.id} idd={i.idd}
                              value={i.value} usedV={i.usedV}> </TableRow>
            )
        });
        var tableMap2 = vouchers_t2.map(function (i) {
            return (<TableRow key={i.id} idd={i.idd}
                              value={i.value} usedV={i.usedV}> </TableRow>
            )
        });
        // define, what will be rendered to the page
        return (
            <div>
         <h3>Figure 14 c - d: Earnings Overview for different examples</h3>
                <table border="2">
                    <tr>
                    <td></td><td>


                                <table id="my_vouchers"
                                       style={{
                                           borderCollapse: "separate",
                                           borderSpacing: 5,
                                           border: "1px solid black",
                                           marginBottom: "0%",
                                           marginTop: "0%",
                                           marginLeft: "0.1%",
                                           backgroundColor: "whitesmoke"
                                       }}
                                >
                                    <thead>
                                    </thead>
                                    <tbody>
                                    <tr>
                                        <td colSpan="4">Units Sold</td>
                                    </tr>
                                    <tr className="units">
                                        <td style={{textAlign: "center"}}><b>Number of Unit</b></td>
                                        <td style={{textAlign: "center"}}><b>Earn of Unit</b></td>
                                        <td style={{backgroundColor: "#c6effb", textAlign: "center"}}><b></b></td>
                                    </tr>
                                      <tr>
                                    <td style={{textAlign: "center"}}>-3</td>
                                    <td>0</td>
                                    <td></td>
                                    </tr>
                                      <tr>
                                    <td style={{textAlign: "center"}}>-2</td>
                                    <td>0</td>
                                    <td></td>
                                    </tr>
                                    <tr>
                                    <td style={{textAlign: "center"}}>-1</td>
                                    <td>0</td>

                                    </tr>
                                    </tbody>
                                </table>


                </td>
                    </tr>
                    <tr>
                        <td width="50%">
                            <table id="my_vouchers"
                                       style={{
                                           borderCollapse: "separate",
                                           borderSpacing: 5,
                                           border: "1px solid black",
                                           marginBottom: "0%",
                                           marginTop: "0%",
                                           marginLeft: "0.1%",
                                           backgroundColor: "whitesmoke"
                                       }}
                                >
                                    <thead>
                                    </thead>
                                    <tbody>
                                    <tr>
                                        <td colSpan="4">Units that must be purchased</td>
                                    </tr>
                                    <tr className="units">
                                        <td style={{textAlign: "center"}}><b>Number of Unit</b></td>
                                        <td style={{textAlign: "center"}}><b>Earn of Unit</b></td>
                                        <td style={{backgroundColor: "#c6effb", textAlign: "center"}}><b>Bought</b></td>
                                    </tr>
                                    {tableMap1}
                                    </tbody>
                                </table>
                        </td>
                        <td width="50%">

                                <table id="my_vouchers"
                                       style={{
                                           borderCollapse: "separate",
                                           borderSpacing: 5,
                                           border: "1px solid black",
                                           marginBottom: "0%",
                                           marginTop: "0%",
                                           marginLeft: "0.1%",
                                           backgroundColor: "whitesmoke"
                                       }}
                                >
                                    <thead>
                                    </thead>
                                    <tbody>
                                    <tr>
                                        <td colSpan="4">Units that must be purchased</td>
                                    </tr>
                                    <tr className="units">
                                        <td style={{textAlign: "center"}}><b>Number of Unit</b></td>
                                        <td style={{textAlign: "center"}}><b>Earn of Unit</b></td>
                                        <td style={{backgroundColor: "#c6effb", textAlign: "center"}}><b>Bought</b></td>
                                    </tr>
                                    {tableMap2}
                                    </tbody>
                                </table>

                        </td>
                    </tr>
                    <tr>
                        <td style={{verticalAlign: "top"}}>
                            <h4>
                                <b>14.c<br/>
                                    Bought 7 Units<br/>
                                    Sold 2 Units <br/>
                                    <i>Net: Bought 5 Units (7-2=5)</i></b></h4>

                        </td>
                        <td style={{verticalAlign: "top"}}>
                            <h4>
                                <b>14.d<br/>
                                    Bought 7 Units<br/>
                                    Sold 2 Units <br/>
                                    Sold 8 Units<br/>
                                    <i>Net: Bought -3 Units (7-2-8=-3)</i></b></h4></td>
                    </tr>
                </table>

            </div>
        )
    }
});

// render to div id="cost_tables"
ReactDOM.render(<Tables/>, document.getElementById("table23"));

