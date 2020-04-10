// TRADING ACCOUNT DISPLAY
// data - mytrading, my cleaned offers
//  key={contract.id}
//                order={contract.order}
//                offer_tiepe={contract.offer_tiepe}
// product={contract.product}
//                unitsCleared={contract.unitsCleared}
//               priceCleared={contract.priceCleared}>
// used fuction
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

var Trading_account_row = React.createClass({
    render: function () {
        if (this.props.offer_tiepe == "0") {
            var cssClass = "SELL";
            var units = this.props.unitsCleared;

        } else {
            var cssClass = "BUY";
            var units = -this.props.unitsCleared;

        }
        ;
        return (<tr className={cssClass}>
                <td>{this.props.order}</td>
                <td>{this.props.product}</td>
                <td>{units}</td>
                <td>{this.props.priceCleared}</td>
            </tr>
        )
    }
});
var Trading_account = React.createClass({
    render: function () {
        var manipulate = JSON.parse(JSON.stringify(this.props.mytrading));
        var manipulate_sorted = manipulate.sort(sort_by("id", false, parseInt));
        var order_start = 1
        for (var key in manipulate_sorted) {
            if (manipulate_sorted.hasOwnProperty(key)) {
                manipulate_sorted[key].order = order_start;
                var order_start = order_start + 1
            }
        }
        var Map_trading = manipulate_sorted.sort(sort_by("id", true, parseInt)).map(function (contract) {
            return ( <Trading_account_row
                key={contract.id}
                order={contract.order}
                offer_tiepe={contract.offer_tiepe}
                product={contract.product}
                unitsCleared={contract.unitsCleared}
                priceCleared={contract.priceCleared}>
            </Trading_account_row>)
        });
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
                <div className="title" style={{marginTop: 10}}>Transactions Overview
                </div>
                <center>
                    <table id="my_vouchers" style={{padding: 10, border: "1px solid black", width: "98%"}}>
                        <thead>
                        </thead>
                        <tbody>
                        <tr>
                            <td style={{textAlign: "center"}}><b>#</b></td>
                            <td style={{textAlign: "center"}}><b>Total</b></td>
                            <td style={{textAlign: "center"}}><b>Units</b></td>
                            <td style={{textAlign: "center"}}><b>Price per Unit</b></td>
                        </tr>
                        {Map_trading}
                        </tbody>
                    </table>
                </center>
            </div>
        )
    }
});

window.Trading_account = Trading_account;