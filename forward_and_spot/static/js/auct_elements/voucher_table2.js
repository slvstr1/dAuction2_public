/// Display Voucher table for Stage 2
// inputs needed:
// role = 0 - PR, 1 - RE
// vouchers = full of voucher objectrs, or empty, if role is 1 (RE)
// player_stats.vouchers_negative - number of negative vouchers
//              .vouchers_used - number of used vouchers
//              .player_demand - demand of the player
//              .vouchers_negative_stage1
//              . vouchers_used_stage1

var TablerowVoucher = React.createClass ({
    render: function () {
        return (<tr><td style={{textAlign: "center"}}>{this.props.idd}</td><td>{this.props.value}</td><td>{this.props.usedV}</td></tr>
        )
        }
});

// Voucher table for 2nd Stage retailer
var Voucher_Table2R = React.createClass({
   render: function () {
          // Stage indicator based on educational settings
        if (this.props.educational == false) {
                    var stage_indicator1 = <span>Stage 1</span>
                    var stage_indicator2 = <span>Stage 2</span>
                } else {
                   var stage_indicator1 = <span>the Forward Market</span>
                   var stage_indicator2 = <span>the Spot Market</span>
                }
       // generate vouchers, if RE
       var my_role = this.props.role;
        if (my_role == 1) {
            var g_vouchers = [];
            for (var i = 0; i < 35; i++) {
                g_vouchers.push({'id': i + 1, 'idd': i + 1, 'value_cum': 0, "value": 0, "auction": 1})
            }
            var voucher_manipulate = g_vouchers;
        } else {
            var voucher_manipulate = JSON.parse(JSON.stringify(this.props.vouchers));
        }
       // voucher logic
       // common for RE and PR, negative vouchers and X
       var begin = 1 - this.props.player_stats.vouchers_negative;
       var end = begin + this.props.player_stats.vouchers_used;
       // add negative if they are any
       if (this.props.player_stats.vouchers_negative > 0) {
           // index array
           var list = [];
           for (var i = begin - 1; i < 0; i++) {
               list.push(i);
           }
           ;
           for (var g in list) {
               voucher_manipulate.push({'id': list[g], 'idd': list[g], "auction": -1, 'value': 0, 'value_cum': 0});
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
       var my_position = this.props.player_stats.vouchers_used - this.props.player_stats.vouchers_negative
       // changes only for RE
           if (this.props.role == 1) {

               for (var key in voucher_manipulate) {
                   if (voucher_manipulate.hasOwnProperty(key)) {
                       // add retail price to nonnegative vouchers
                       if (voucher_manipulate[key].auction != -1 && voucher_manipulate[key].idd > 0 && voucher_manipulate[key].idd <= this.props.player_stats.player_demand) {
                           voucher_manipulate[key].value = this.props.auction.retail_price;
                           voucher_manipulate[key].value_cum = this.props.auction.retail_price;
                       } else {
                           voucher_manipulate[key].value = 0;
                           voucher_manipulate[key].value_cum = 0;
                       }
                   }
               }
               // sum values
               for (var key in voucher_manipulate) {
                   if (voucher_manipulate.hasOwnProperty(key) && voucher_manipulate[key].auction != -1) {
                       if (key > 0) {
                           voucher_manipulate[key].value_cum = voucher_manipulate[key].value_cum + voucher_manipulate[key - 1].value_cum;
                       }

                   }
               }
           }
       var total_d = this.props.player_stats.player_demand;

           var v_negative = $.grep(voucher_manipulate, function (n, i) {
               return n.idd <= 0;
           });
           var v_less10lessO = $.grep(voucher_manipulate, function (n, i) {
               return n.idd <= 10 && n.idd <= total_d && n.idd > 0;
           });
           var v_more10lessO = $.grep(voucher_manipulate, function (n, i) {
               return n.idd >= 11 && n.idd <= total_d && n.idd > 0;
           });
           var v_excess = $.grep(voucher_manipulate, function (n, i) {
               return n.idd > total_d && n.idd > 0 && n.usedV=="X";
           });
           var v_notpurchased = $.grep(voucher_manipulate, function (n, i) {
               return n.idd > total_d && n.idd > 0 && n.usedV!="X";
           });

       var tableMap1 = v_negative.map(function (contract) {
           return (<TablerowVoucher key={contract.id} idd={contract.idd} value_cum={contract.value_cum}
                                    value={contract.value} usedV={contract.usedV}> </TablerowVoucher>
           )
       });
       var tableMap2 = v_less10lessO.map(function (contract) {
           return (<TablerowVoucher key={contract.id} idd={contract.idd} value_cum={contract.value_cum}
                                    value={contract.value} usedV={contract.usedV}> </TablerowVoucher>
           )
       });
       var tableMap3 = v_more10lessO.map(function (contract) {
           return (<TablerowVoucher key={contract.id} idd={contract.idd} value_cum={contract.value_cum}
                                    value={contract.value} usedV={contract.usedV}> </TablerowVoucher>
           )
       });
       var tableMap4 = v_excess.map(function (contract) {
           return (<TablerowVoucher key={contract.id} idd={contract.idd} value_cum={contract.value_cum}
                                    value={contract.value} usedV={contract.usedV}> </TablerowVoucher>
           )
       });
            var tableMap5 = v_notpurchased.map(function (contract) {
           return (<TablerowVoucher key={contract.id} idd={contract.idd} value_cum={contract.value_cum}
                                    value={contract.value} usedV={contract.usedV}> </TablerowVoucher>
           )
       });
    if (this.props.role == 1) {
        var x_title = "Bought";
        var x_title_sm = 'bought';
        var title = "Retailer - Earnings overview";
        var Tab1 = "Units sold";
        var Tab2 = "Units that must be purchased";
        var Tab3 = "Units that must be purchased:";
        var Tab4 = "Excess units, can be sold";
        var Tab5 = "Not purchased not needed units";
        var ClassNam = "BUY";
        var tableIdVal = "Number of Unit";
        var tableVal = "Earn of Unit";
    }
    // table headings for PR
    if (this.props.role == 0) {
        var x_title = "Sold";
        var x_title_sm = 'sold';
        var title = "Producer - Production overview";
        var Tab1 = "Units bought";
        var Tab2 = "Units that must be sold";
        var Tab3 = "Units that must be sold:";
        var Tab4 = "Sold units over minimal quota";
        var Tab5 = "Not sold units";
        var ClassNam = "SELL";
        var tableIdVal = "Number of Unit";
        var tableVal = "Cost of Unit";

    }
    // show 2nd units that must be purchased table based on demanded number
    if (this.props.player_stats.player_demand > 10) {
    // show both of them
    var must_tables = <div>
            <table id="my_vouchers"
                               style={{
                                   borderCollapse: "separate",
                                   borderSpacing: 5,
                                   border: "5px solid black",
                                   marginBottom: "3%",
                                   marginTop: "3%",
                                   marginLeft: "3%"
                               }}>
                            <thead>
                            <tr>
                                <td colSpan="4">{Tab3}</td>
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
    </div>
    } else {
        // show only one
        var must_tables = <div>
        </div>
    }
    // indicate vouchers used in Stage 1 if not only spot
    if (this.props.only_spot) {
          var prev_vouchers = <div></div>
    } else {
        if (this.props.player_stats.vouchers_negative_stage1 > 0) {
            var prev_vouchers = <div>You had {this.props.player_stats.vouchers_negative_stage1} negative units
                in {stage_indicator1}.</div>
        } else if (this.props.player_stats.vouchers_used_stage1 > 0) {
            var prev_vouchers = <div>You {x_title_sm} {this.props.player_stats.vouchers_used_stage1} units
                in {stage_indicator1}.</div>
        } else {
            var prev_vouchers = <div>You have not {x_title_sm} any units in {stage_indicator1}.</div>
        }
    }
    return (
        <div
            style={{
                margin: "1% 1% 1% 1%",
                backgroundColor: "whitesmoke",
                position: "absolute",
                top: 0,
                bottom: 0,
                left: 0,
                right: 0
            }}>
            <div style={{left: 0, right: 0, top: 0, bottom: "95%", position: "absolute"}}>
                <center><h3 className={ClassNam}>{title}</h3></center>
                <div> {prev_vouchers} </div>
            </div>

            <div
                style={{
                    display: "inline-block",
                    right: "50%",
                    left: 0,
                    top: "7%",
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

                               }}>
                            <thead>
                            </thead>
                            <tbody>
                            <tr>
                                <td colSpan="4">{Tab1}</td>
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
                               style={{borderCollapse: "separate", borderSpacing: 5, border: "5px solid black"}}>
                            <thead>
                            </thead>
                            <tbody>
                            <tr>
                                <td colSpan="4">{Tab2}</td>
                            </tr>
                            <tr className="units">
                                <td style={{textAlign: "center"}}><b>{tableIdVal}</b></td>
                                <td style={{textAlign: "center"}}><b>{tableVal}</b></td>
                                <td className={ClassNam}><b>{x_title}</b></td>
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
                     top: "7%",
                     bottom: "20%",
                     position: "absolute"
                 }}>
                <div style={{float: 'center'}}>
                    <center>
                        {must_tables}
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
                                <td colSpan="4">{Tab4}</td>
                            </tr>
                            <tr className="units">
                                <td style={{textAlign: "center"}}><b>{tableIdVal}</b></td>
                                <td style={{textAlign: "center"}}><b>{tableVal}</b></td>
                                <td className={ClassNam}>
                                    <b>{x_title}</b></td>
                            </tr>
                            </thead>
                            <tbody>
                            {tableMap4}
                            </tbody>
                        </table>
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
                                <td colSpan="4">{Tab5}</td>
                            </tr>
                            <tr className="units">
                                <td style={{textAlign: "center"}}><b>{tableIdVal}</b></td>
                                <td style={{textAlign: "center"}}><b>{tableVal}</b></td>
                                <td className={ClassNam}>
                                    <b>{x_title}</b></td>
                            </tr>
                            </thead>
                            <tbody>
                            {tableMap5}
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
    )}
});

window.Voucher_Table2R = Voucher_Table2R;
