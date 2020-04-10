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
        // ***

        // Example for Marcel, how to generate vouchers for Retailer
        /// in the case of PR, we are taking already made voucher objects from "vouchers" variable, imported from Django
        /// every voucher object contains different cost
        /// in the case of RE, the value of each voucher is the same, and we need to generate them inside JS using retailer_value as
        /// their value, to demonstrate
        // RE, generate 10 vouchers
        /// take value from treatment object
        var value = treatment.retail_price;
        var totearnings = treatment.retail_price * 7;
        var totprofit = treatment.retail_price * 7 - 19;
        /// initialize empty array
        var g_vouchers = [];
        /// create 10 vouchers via loop, we need id to use it as a key in react and idd to display voucher # in table
        for (var i = 0; i < 5; i++) {
            g_vouchers.push({'id': i + 1, 'idd': i + 1, "value": value})
        }
        /// copy to two arrays, used in table
        var vouchers_t1 = JSON.parse(JSON.stringify(g_vouchers));
        var vouchers_t2 = JSON.parse(JSON.stringify(g_vouchers));
        /// now make Xs in vouchers
        /// in the first table, there is none, in the second, there is 7 of them
        for (var key in vouchers_t2) {
            if (vouchers_t2.hasOwnProperty(key)) {
                vouchers_t2[key].usedV = "";
                if (vouchers_t2[key].idd <= 7) {
                    vouchers_t2[key].usedV = "X";
                }
            }
        }
        /// now, I have my voucher objects, and I need to use map function on row object, TableRow, to make a dynamic table
         // map to tables using row object
        var tableMap1 = vouchers_t1.map(function (i) {
            return (<TableRow key={i.id} idd={i.idd}
                              value={i.value} usedV={i.usedV}> </TableRow>
            )
        });


        return (
            <div style={{zoom: 1.5}}>
            <center>
                    <table>
                        <thead><tr><center><div style={{backgroundColor: "whitesmoke"}}><strong>Profit Overview</strong></div></center></tr></thead>
                        <tbody style={{backgroundColor: "whitesmoke"}}>
                        <tr>
                            <td>
                                <div align="center" className="panel panel-warning">
                                    <strong>
                                      Total Earnings</strong>   : {totearnings} (this round)
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <p>Trading Revenue Stage 1: 0 </p>
                                <div align="center" className="panel panel-warning">
                                    <p><strong>
                                        Trading Revenues: -19 </strong>(this Stage)
                                    </p>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div align="center" className="panel panel-warning">
                                    <strong>
                                      PROFIT :  {totprofit}</strong>  (this round)
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>
            </center>
            </div>
        )
    }
});
ReactDOM.render(<Tables/>, document.getElementById("table25"));
