
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


var VouchersNegat = React.createClass({
    render: function () {
        var vouchers_p = this.props.vouchers_p;
        var vouchers_n = this.props.vouchers_n;
        var role = this.props.role;
        var style = {backgroundColor: " #c6effb", textAlign: "center"};
        var title1 = 'Units sold';
        var title2 = 'Units that must be purchased';
        var x_title = "Bought";
        if (role == "PR") {
            var style = {backgroundColor: "#fba0a0", textAlign: "center"};
            var title2 = 'Units that can be sold';
            var x_title = 'Sold';
        }

        var tableMap_n = vouchers_n.map(function (i) {
            return (<TableRow key={i.id} idd={i.idd}
                              value={i.value} usedV={i.usedV}> </TableRow>
            )
        });
        var tableMap_p = vouchers_p.map(function (i) {
            return (<TableRow key={i.id} idd={i.idd}
                              value={i.value} usedV={i.usedV}> </TableRow>
            )
        });
        return (
            <div>
                <div >
                    <table id="my_vouchers"
                           style={{
                                       backgroundColor: "whitesmoke",
                                           borderCollapse: "separate",
                                           borderSpacing: 5,
                                           border: "1px solid black",
                                           marginBottom: "3%",
                                           marginTop: "3%",
                                           marginLeft: "0.1%"
                                       }}
                    >
                        <thead>
                        </thead>
                        <tbody>
                        <tr>
                            <td colSpan="4">{title1}</td>
                        </tr>
                        <tr className="units">
                            <td style={{textAlign: "center"}}><b>Number of units</b></td>
                            <td style={{textAlign: "center"}}><b>Cost per unit</b></td>
                            <td style={{textAlign: "center", color: "whitesmoke", userSelect:"none"}}>{x_title}</td>
                        </tr>
                        {tableMap_n}
                        </tbody>
                    </table>
                </div>
                <div >
                    <table id="my_vouchers"
                           style={{
                                       backgroundColor: "whitesmoke",
                                           borderCollapse: "separate",
                                           borderSpacing: 5,
                                           border: "1px solid black",
                                           marginBottom: "3%",
                                           marginTop: "3%",
                                           marginLeft: "0.1%"
                                       }}
                    >
                        <thead>
                        </thead>
                        <tbody>
                        <tr>
                            <td colSpan="4">{title2}</td>
                        </tr>
                        <tr className="units">
                            <td style={{textAlign: "center"}}><b>Number of units</b></td>
                            <td style={{textAlign: "center"}}><b>Cost per unit</b></td>
                            <td style={style}><b>{x_title}</b></td>
                        </tr>
                        {tableMap_p}
                        </tbody>
                    </table>
                </div>
            </div>
        )
    }
});


window.VouchersNegat = VouchersNegat;