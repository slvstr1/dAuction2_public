/// Display Voucher table for Stage 1
// inputs needed:
// role = 0 - PR, 1 - RE
// vouchers = full of voucher objectrs, or empty, if role is 1 (RE)
// player_stats.vouchers_negative - number of negative vouchers
//              .vouchers_used - number of used vouchers


var TablerowVoucher = React.createClass({
    render: function () {
        return (<tr>
                <td style={{textAlign: "center"}}>{this.props.idd}</td>
                <td>{this.props.value}</td>
                <td>{this.props.usedV}</td>
            </tr>
        )
    }
});
// create table
var Voucher_Table = React.createClass({
    render: function () {
        // if im a retailer, vouchers are not provided, have to be generated
        var my_role = this.props.role;
        if (my_role == 1) {
            var g_vouchers = [];
            for (var i = 0; i < 35; i++) {
                g_vouchers.push({'id': i + 1, 'idd': i + 1, 'value_cum': 0, "value": 0, "auction": 1})
            }
            var vouchers = g_vouchers;
        } else {
            var vouchers = JSON.parse(JSON.stringify(this.props.vouchers));
        }

        // common for RE and PR, negative vouchers and X
        var begin = 1 - this.props.player_stats.vouchers_negative;
        var end = begin + this.props.player_stats.vouchers_used;
        var voucher_manipulate = vouchers;
        // add negative if they are any
        if (this.props.player_stats.vouchers_negative > 0) {
            // index array
            var list = [];
            for (var i = begin - 1; i < 0; i++) {
                list.push(i);
            }
            ;
            for (var x in list) {
                voucher_manipulate.push({'id': list[x], 'idd': list[x], "auction": -1, 'value': 0, 'value_cum': 0});
            }
        }
        // add Xes
        for (var key in voucher_manipulate) {
            if (voucher_manipulate.hasOwnProperty(key)) {
                voucher_manipulate[key].usedV = "";
                if (voucher_manipulate[key].idd >= begin && voucher_manipulate[key].idd < end) {
                    voucher_manipulate[key].usedV = "X";
                }
            }
        }

        // split for RE, PR
        // if producer
        if (my_role == 0) {
            var x_title = "Sold";
            var v_manipulateS2 = voucher_manipulate;
            var min = Infinity, max = -Infinity, x;
            for (x in v_manipulateS2) {
                if (v_manipulateS2[x].value_cum < min) min = v_manipulateS2[x].value_cum;
                if (v_manipulateS2[x].value_cum > max) max = v_manipulateS2[x].value_cum;
            }
            for (var key in v_manipulateS2) {
                if (v_manipulateS2.hasOwnProperty(key)) {
                    if (v_manipulateS2[key].value_cum == -1) {
                        v_manipulateS2[key].value_cum = max;
                    }

                }
            }
            var v_negative = $.grep(v_manipulateS2, function (n, i) {
                return n.idd <= 0;
            });
            var v_less10 = $.grep(v_manipulateS2, function (n, i) {
                return n.idd <= 10 & n.idd > 0;
            });
            var v_more10 = $.grep(v_manipulateS2, function (n, i) {
                return n.idd > 10 & n.idd <= 35;
            });
            var tableMap1 = v_negative.map(function (contract) {
                return (<TablerowVoucher key={contract.id} idd={contract.idd}
                                         value={contract.value} usedV={contract.usedV}> </TablerowVoucher>
                )
            });
            var tableMap2 = v_less10.map(function (contract) {
                return (<TablerowVoucher key={contract.id} idd={contract.idd}
                                         value={contract.value} usedV={contract.usedV}> </TablerowVoucher>
                )
            });
            var tableMap3 = v_more10.map(function (contract) {
                return (<TablerowVoucher key={contract.id} idd={contract.idd}
                                         value={contract.value} usedV={contract.usedV}> </TablerowVoucher>
                )
            });
            // table labels
            var TableHeading = "Producer - Production overview";
            var Table1Units1 = "Units bought";
            var Table1Units2 = "(can be resold)";
            var Table2Units = "Units that can be sold";
            var Table4Units = "Units that can be sold"
            var ClassNam = "SELL";
            var tableVal = "Cost of Unit";
            var tableTotalVal = "Total Cost";
            var tableIdVal = "Number of Unit";
        } else {
            var x_title = "Bought";
            var v_manipulateS1 = voucher_manipulate;
            for (var key in v_manipulateS1) {
                if (v_manipulateS1.hasOwnProperty(key) && v_manipulateS1[key].auction != -1) {
                    v_manipulateS1[key].value = "?";
                    v_manipulateS1[key].value_cum = "?";
                }

            }
            var v_negative = $.grep(v_manipulateS1, function (n, i) {
                return n.idd <= 0;
            });
            var v_less10 = $.grep(v_manipulateS1, function (n, i) {
                return n.idd <= 10 & n.idd > 0;
            });
            var v_more10 = $.grep(v_manipulateS1, function (n, i) {
                return n.idd > 10 & n.idd <= 35;
            });
            var tableMap1 = v_negative.map(function (contract) {
                return (<TablerowVoucher key={contract.id} idd={contract.idd}
                                         value={contract.value} usedV={contract.usedV}> </TablerowVoucher>
                )
            });
            var tableMap2 = v_less10.map(function (contract) {
                return (<TablerowVoucher key={contract.id} idd={contract.idd}
                                         value={contract.value} usedV={contract.usedV}> </TablerowVoucher>
                )
            });
            var tableMap3 = v_more10.map(function (contract) {
                return (<TablerowVoucher key={contract.id} idd={contract.idd}
                                         value={contract.value} usedV={contract.usedV}> </TablerowVoucher>
                )
            });
            // table labels
            var TableHeading = "Retailer - Earnings Overview";
            var Table1Units1 = "Units sold";
            var Table1Units2 = "(must be repurchased)";
            var Table2Units = "Units bought";
            var Table4Units = "Units bought"
            var ClassNam = "BUY";
            var tableVal = "Earn of Unit";
            var tableTotalVal = "Total Earn";

            var tableIdVal = "Number of Unit";
        }

        return (
            <div
                style={{
                    margin: "5px 5px 5px 5px",
                    backgroundColor: "whitesmoke",
                    position: "absolute",
                    top: 0,
                    bottom: 0,
                    left: 0,
                    right: 0
                }}>
                <div style={{left: 0, right: 0, top: 0, bottom: "95%", position: "absolute"}}>
                    <center><h3 className={ClassNam}> {TableHeading} </h3></center>
                </div>
                <div
                    style={{
                        display: "inline-block",
                        right: "50%",
                        left: 0,
                        top: "5%",
                        bottom: "20%",
                        position: "absolute"
                    }}>
                    <div style={{float: 'center'}}>
                        <center>
                            <table id="my_vouchers"
                                   style={{
                                       borderCollapse: "separate",
                                       borderSpacing: 5,
                                       border: "1px solid black",
                                    marginBottom: "3%",
                                   marginTop: "3%",
                                   marginLeft: "0.1%"
                                   }}>
                                <thead>
                                </thead>
                                <tbody>
                                <tr>
                                    <td colSpan="4">{Table1Units1}
                                        <div>{Table1Units2}</div>
                                    </td>
                                </tr>
                                <tr className="units">
                                    <td style={{textAlign: "center"}}><b>{tableIdVal}</b></td>
                                    <td style={{textAlign: "center"}}><b>{tableVal}</b></td>
                                    <td style={{textAlign: "center", color: "whitesmoke", userSelect:"none"}}>{x_title}</td>
                                </tr>
                                {tableMap1}
                                </tbody>
                            </table>
                        </center>
                    </div>
                    <div style={{float: 'center', clear: "center"}}>
                        <center>
                            <table id="my_vouchers"
                                   style={{borderCollapse: "separate", borderSpacing: 5, border: "1px solid black"}}>
                                <thead>
                                </thead>
                                <tbody>
                                <tr>
                                    <td colSpan="4">{Table2Units}</td>
                                </tr>
                                <tr className="units">
                                    <td style={{textAlign: "center"}}><b>{tableIdVal}</b></td>
                                    <td style={{textAlign: "center"}}><b>{tableVal}</b></td>
                                    <td className={ClassNam} style={{textAlign: "center"}}><b>{x_title}</b></td>
                                </tr>
                                {tableMap2}
                                </tbody>
                            </table>
                        </center>
                    </div>
                </div>
                <div id="div1"
                     style={{
                         display: "inline-block",
                         verticalAlign: "top",
                         left: "50%",
                         right: 0,
                         top: "5%",
                         bottom: "20%",
                         position: "absolute"
                     }}>
                    <div style={{float: 'center'}}>
                        <center>
                            <table id="my_vouchers"
                                   style={{
                                       borderCollapse: "separate",
                                       borderSpacing: 5,
                                       border: "1px solid black",
 marginBottom: "3%",
                                   marginTop: "3%",
                                   marginLeft: "3%"
                                   }}>
                                <thead>
                                <tr>
                                    <td colSpan="4">{Table2Units}</td>
                                </tr>
                                <tr className="units">
                                    <td style={{textAlign: "center"}}><b>{tableIdVal}</b></td>
                                    <td style={{textAlign: "center"}}><b>{tableVal}</b></td>
                                    <td className={ClassNam}>
                                        <b>{x_title}</b></td>
                                </tr>
                                </thead>
                                <tbody>
                                {tableMap3}
                                </tbody>
                            </table>
                        </center>
                    </div>
                    <div style={{float: 'center', clear: "center"}}>
                        <center>
                        </center>
                    </div>
                </div>
            </div>
        )
    }
});


window.Voucher_Table = Voucher_Table;
