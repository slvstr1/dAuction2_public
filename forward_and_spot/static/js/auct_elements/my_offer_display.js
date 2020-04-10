/// MY STANDING OFFER TABLE
// displays my standing offers under Submit and offer, contains cancel offer function
// needs
// data = my_standing offers, standard offer type
//  id, priceOriginal, unitsAvailable, offer_tiepe
//
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

var Tablerow = React.createClass({
    handleCancelOffer: function (e) {
        // returns number of my offer
        var offer_id = e.target.value;
        var group_id = window.group_id;
        var data = {"offer_id": offer_id, "group_id": group_id};
        $.ajax({
            type: "POST",
            url: "/api/cancel_offer/",
            data: data,
            success: function (data, status) {
                 $('#' + offer_id).text('Canceling...');
                  $('#' + offer_id).prop("disabled", true);
            },
            error: function (type, status, error) {
            console.log(type)
                 $('#' + offer_id).text('Error!');
            }
        });
    }.bind(this),
    render: function () {
        var cssClass = (this.props.offer_tiepe == 0 ? "SELL" : "BUY");
        var Ctype = (this.props.offer_tiepe == 0 ? "SELL" : "BUY");
        return (<tr className={cssClass}>
                <td>{this.props.order}</td>
                <td>{this.props.priceOriginal}</td>
                <td>{this.props.unitsAvailable}</td>
                <td>{Ctype}</td>
                <td>
                    <button id={this.props.id} onClick={this.handleCancelOffer} value={this.props.id}>Cancel</button>
                </td>
            </tr>
        )
    }
});

var My_offers = React.createClass({
    // render the table
    getInitialState: function () {
        return {data: []};
    },
    render: function () {
        // sorting and adding id
        var ma_data = JSON.parse(JSON.stringify(this.props.data));
        var ma_sorted = ma_data.sort(sort_by("id", false, parseInt));
        var order_start = 1
        for (var key in ma_sorted) {
            if (ma_sorted.hasOwnProperty(key)) {
                ma_sorted[key].order = order_start;
                var order_start = order_start + 1
            }
        }
        // logs
        var MyOfferTable = ma_sorted.map(function (contract) {
            return (<Tablerow key={contract.id} id={contract.id} order={contract.order} priceOriginal={contract.priceOriginal}
                              unitsAvailable={contract.unitsAvailable} offer_tiepe={contract.offer_tiepe}>
                </Tablerow>
            );
        });
        return (
            <div id="my_standing_offer"
                 style={{margin: "5px 5px 5px 5px", position: "absolute", top: 0, bottom: 0, left: 0, right: 0}}>
                <div className="title">My Offers Overview</div>
                <table style={{width: "100%", display: "table"}}>
                    <thead></thead>
                    <tbody>
                    <tr style={{textAlign: "center"}}>
                        <td>#</td>
                        <td>Price</td>
                        <td>Units</td>
                        <td>SELL or BUY</td>
                    </tr>
                    {MyOfferTable}
                    </tbody>
                </table>
            </div>
        )}
    });

window.My_offers = My_offers;