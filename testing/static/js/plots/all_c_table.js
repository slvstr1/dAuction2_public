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
                <td className="units" style={{textAlign: "center"}}> {this.props.p}</td >
                <td className="units" style={{textAlign: "center"}}> {this.props.q}</td >

            </tr >
        )
    }
});

var TablerowBuy = React.createClass({
    render: function () {
        return (
            <tr>
                <td className="units" style={{textAlign: "center"}}> {this.props.p}</td >
                <td className="units" style={{textAlign: "center"}}> {this.props.q}</td>
            </tr>
        )
    }
});

// create table
var AllContractsTable = React.createClass({

    render() {

        var setSS = this.props.sell_o;
        var setBB = this.props.buy_o;
        var n = this.props.n;
        if (setSS.length > 0) {
            var mapSell = setSS.map(function (contract) {
                return ( <TablerowSell key={contract.id}
                                       q={contract.q}
                                       p={contract.p}>
                    </TablerowSell>
                )
            });
        } else {
            var mapSell = <tr>
                <td></td>
                <td></td>
            </tr>;
        }
        if (setBB.length > 0) {
            var mapBuy = setBB.map(function (contract) {
                return ( <TablerowBuy key={contract.id}
                                      q={contract.q}
                                      p={contract.p}>
                    </TablerowBuy>
                )
            });
        } else {
            var mapBuy = <tr>
                <td></td>
                <td></td>
            </tr>;

        }
        if (n == 2) {
            var table_class = "col-lg-6"
        } else {
            var table_class = "col-lg-7"
            var table_style = ""
        }
        return (
            <div className={table_class} style={{ fontSize: "150%", backgroundColor: "WhiteSmoke", padding: 0}}>
                <table style={{width: "100%", emptyCells: "show"}}>
                    <tr>
                        <td>
                            <center>
                                <div style={{fontWeight: 900, textAlign: "center", width:"inherit"}}>Offers Overview
                                </div>
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
                                            <th style={{backgroundColor: "#fba0a0",textAlign: "center",fontWeight: 900, fontSize: "110%"}}
                                                colSpan="3"> SELL
                                            </th >
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
                                            <th style={{backgroundColor: "#c6effb",textAlign: "center",fontWeight: 900, fontSize: "110%"}}
                                                colSpan="3"> BUY
                                            </th >
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