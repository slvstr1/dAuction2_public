// Master elements for the table

var Voucher_master2 = React.createClass({

    render() {
        var treatment_d = (($('#treatment_js').text()).replace(/\'/g, '\"')).replace(/\False/g, '0').replace(/\True/g, '1');
        var vouchers_d = (($('#vouchers_js').text()).replace(/\'/g, '\"')).replace(/\False/g, '0').replace(/\True/g, '1');
        var treatment = $.parseJSON(treatment_d);
        var vouchers = $.parseJSON(vouchers_d);
        // RE
        var value = treatment.retail_price;
        var g_vouchers = [];
        for (var i = 0; i < 10; i++) {
            g_vouchers.push({'id': i + 1, 'idd': i + 1, 'value_cum': 0, "value": value, "treatment": 1})
        }
        var n_vouchers = [];
        for (var i = 0; i < 2; i++) {
            n_vouchers.push({'id': i + 1, 'idd': -2 + i, 'value_cum': 0, "value": 0, "treatment": 1})
        }

        return (
            <div>
                <VouchersNegat role="RE" vouchers_p={g_vouchers} vouchers_n={n_vouchers}/>
            </div>
        )
    }
});

ReactDOM.render(<Voucher_master2/>, document.getElementById("content1"));


var Voucher_master1 = React.createClass({

    render() {
        var treatment_d = (($('#treatment_js').text()).replace(/\'/g, '\"')).replace(/\False/g, '0').replace(/\True/g, '1');
        var vouchers_d = (($('#vouchers_js').text()).replace(/\'/g, '\"')).replace(/\False/g, '0').replace(/\True/g, '1');
        var treatment = $.parseJSON(treatment_d);
        var vouchers = $.parseJSON(vouchers_d);
        // RE
        var value = treatment.retail_price;
        var g_vouchers = [];
        for (var i = 0; i < 10; i++) {
            g_vouchers.push({'id': i + 1, 'idd': i + 1, 'value_cum': 0, "value": value, "treatment": 1})
        }
        for (var key in g_vouchers) {
            if (g_vouchers.hasOwnProperty(key)) {
                g_vouchers[key].usedV = "";
                if (g_vouchers[key].idd <= 3) {
                    g_vouchers[key].usedV = "X";
                }
            }
        }
        return (
            <div>
                <VouchersBasic role="RE" vouchers={g_vouchers}/>
            </div>
        )
    }
});

ReactDOM.render(<Voucher_master1/>, document.getElementById("content3"));
