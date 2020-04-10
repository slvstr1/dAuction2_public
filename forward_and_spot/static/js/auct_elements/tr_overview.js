// OVERVIEW OF STANDING MARKET TRANSACTIONS
// data
// contracts : active offers, sell or buy
//      id, offer_tiepe, priceOriginal, unitsAvailible


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


// ALL STANDING MARKET OFFERS TABLE
var TablerowSell = React.createClass({
    render: function () {
        return (
            <tr>
                <td className="units" style={{textAlign: "center"}}> {this.props.priceOriginal}</td >
                <td className="units" style={{textAlign: "center"}}> {this.props.unitsAvailable}</td >

            </tr >
        )
    }
});

var TablerowBuy = React.createClass({
    render: function () {
        return (
            <tr>
                <td className="units" style={{textAlign: "center"}}> {this.props.priceOriginal}</td >
                <td className="units" style={{textAlign: "center"}}> {this.props.unitsAvailable}</td>
            </tr>
        )
    }
});

// create table
var AllContractsTable = React.createClass({
    // define render method, rendered as two tables beside each other in <div> container
    render() {
        //sum transactions with same p to one q
        var active_offers_copy = JSON.parse(JSON.stringify(this.props.contracts));
        var setS = $.grep(active_offers_copy, function (n, i) {
            return n.offer_tiepe == "0";
        });
        var setB = $.grep(active_offers_copy, function (n, i) {
            return n.offer_tiepe == "1";
        });
        // sort json objects by price
        setS.sort(sort_by("priceOriginal", true, parseInt));
        setB.sort(sort_by("priceOriginal", false, parseInt));
        // sum contracts with same price to one with summed quantity
        for (var key in setS) {
            if (setS.hasOwnProperty(key)) {
                if (key > 0) {
                    if (setS[key].priceOriginal == setS[key - 1].priceOriginal) {
                        var total_q = setS[key].unitsAvailable + setS[key - 1].unitsAvailable;
                        setS[key].unitsAvailable = total_q;
                        delete  setS[key - 1];
                    }
                }
            }
        }
        for (var key in setB) {
            if (setB.hasOwnProperty(key)) {
                if (key > 0) {
                    if (setB[key].priceOriginal == setB[key - 1].priceOriginal) {
                        var total_q = setB[key].unitsAvailable + setB[key - 1].unitsAvailable;
                        setB[key].unitsAvailable = total_q;
                        delete  setB[key - 1];
                    }
                }
            }
        }
        // create rolling total of quantity
        var total = 0;
        for (var key in setS) {
            if (setS.hasOwnProperty(key)) {
                var ik = setS[key].unitsAvailable;
                total = total + Number(ik);
                setS[key].totalU = Number(total);
            }
        }
        var total = 0;
        for (var key in setB) {
            if (setB.hasOwnProperty(key)) {
                var ik = setB[key].unitsAvailable;
                total = total + Number(ik);
                setB[key].totalUs = Number(total);
            }
        }
        // sort the sets before cutting
        // set Sell offers
        setS.sort(sort_by("priceOriginal", false, parseInt))
        // set Buy offers
        setB.sort(sort_by("priceOriginal", true, parseInt));
        // use only fist X elements
        var setSS = setS.slice(0, 6);
        var setBB = setB.slice(0, 7);
        // resort first X elements for display in the interface
        setSS.sort(sort_by("priceOriginal", true, parseInt));
        setBB.sort(sort_by("priceOriginal", true, parseInt));
        var mapSell = setSS.map(function (contract) {
            return ( <TablerowSell key={contract.id}
                                   unitsAvailable={contract.unitsAvailable}
                                   priceOriginal={contract.priceOriginal}>
                </TablerowSell>
            )
        });
        var mapBuy = setBB.map(function (contract) {
            return ( <TablerowBuy key={contract.id}
                                  unitsAvailable={contract.unitsAvailable}
                                  priceOriginal={contract.priceOriginal}>
                </TablerowBuy>
            )
        });
        return (
            <div id="set_offer">
                <table style={{width: "100%", emptyCells: "show"}}>
                    <tr>
                        <td>
                            <center>
                                <div className="title">Offers Overview</div>
                            </center>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div>
                                <div style={{height: "11em", overflow: "hidden"}}>
                                    <table style={{width: "100%"}}>
                                        <thead>
                                        <tr>
                                            <th className="SELLb" colSpan="3"> SELL</th >
                                        </tr>
                                        <tr>
                                            <td className="units" style={{textAlign: "center"}}> &nbsp; <b>Price per
                                                Unit</b></td>
                                            <td className="units" style={{textAlign: "center"}}> &nbsp; <b>Number of
                                                Units</b></td>
                                        </tr>
                                        </thead>
                                        <tbody>
                                        {mapSell}
                                        </tbody>
                                        <tfoot >
                                        </tfoot >
                                    </table>
                                </div>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td>&nbsp;</td>
                    </tr>
                    <tr>
                        <td>
                            <div>
                                <div style={{height: "9.5em", overflow: "hidden"}}>
                                    <table style={{width: "100%"}}>
                                        <thead >
                                        <tr>
                                            <th className="BUYb" colSpan="3"> BUY</th >
                                        </tr>
                                        <tr>

                                            <td className="units" style={{textAlign: "center"}}> &nbsp; <b>Price per
                                                Unit</b></td >
                                            <td className="units" style={{textAlign: "center"}}> &nbsp; <b> Number of
                                                Units</b></td >
                                        </tr>
                                        </thead>
                                        <tbody>
                                        {mapBuy}
                                        </tbody>
                                        <tfoot>
                                        </tfoot>
                                    </table >
                                </div>
                            </div>
                        </td>
                    </tr>
                </table>
            </div>
        )
    }
});

window.AllContractsTable = AllContractsTable;