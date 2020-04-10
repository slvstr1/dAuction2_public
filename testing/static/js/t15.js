// Master elements for the table

var Voucher_master1 = React.createClass({

    render() {
        var auction_d = (($('#auction_js').text()).replace(/\'/g, '\"')).replace(/\False/g, '0').replace(/\True/g, '1');
        var vouchers_d = (($('#vouchers_js').text()).replace(/\'/g, '\"')).replace(/\False/g, '0').replace(/\True/g, '1');
        var auction = $.parseJSON(auction_d);
        var vouchers = $.parseJSON(vouchers_d);
        // PR
        var vouchers_10 = vouchers.slice(0, 10);
        var vouchers_t2 = JSON.parse(JSON.stringify(vouchers_10));

        for (var key in vouchers_t2) {
            if (vouchers_t2.hasOwnProperty(key)) {
                vouchers_t2[key].usedV = "";
                if (vouchers_t2[key].idd <= 5) {
                    vouchers_t2[key].usedV = "X";
                }
            }
        }

        return (
            <div>
                <VouchersBasic role="PR" vouchers={vouchers_t2}/>
            </div>
        )
    }
});

ReactDOM.render(<Voucher_master1/>, document.getElementById("content1"));

var Voucher_master2 = React.createClass({
    render() {
        var auction_d = (($('#auction_js').text()).replace(/\'/g, '\"')).replace(/\False/g, '0').replace(/\True/g, '1');
        var vouchers_d = (($('#vouchers_js').text()).replace(/\'/g, '\"')).replace(/\False/g, '0').replace(/\True/g, '1');
        var auction = $.parseJSON(auction_d);
        var vouchers = $.parseJSON(vouchers_d);
        // PR
        var vouchers_10 = vouchers.slice(0, 10);
        var vouchers_t2 = JSON.parse(JSON.stringify(vouchers_10));
        for (var key in vouchers_t2) {
            if (vouchers_t2.hasOwnProperty(key)) {
                vouchers_t2[key].usedV = "";
                if (vouchers_t2[key].idd <= 3) {
                    vouchers_t2[key].usedV = "X";
                }
            }
        }

        return (
            <div>
                <VouchersBasic role="PR" vouchers={vouchers_t2}/>
            </div>
        )
    }
});

ReactDOM.render(<Voucher_master2/>, document.getElementById("content3"));
