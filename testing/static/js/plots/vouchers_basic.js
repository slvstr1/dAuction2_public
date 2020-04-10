
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


var VouchersBasic = React.createClass({
    render: function () {
        var vouchers = this.props.vouchers;
        var role = this.props.role;
        var style = {backgroundColor: " #c6effb", textAlign: "center"};
        var title = 'Units that must be purchased';
        var x_title = "Bought";
        if (role == "PR") {
            var style = {backgroundColor: "#fba0a0", textAlign: "center"};
            var title = 'Units that can be sold';
            var x_title = 'Sold';
        }

        var tableMap = vouchers.map(function (i) {
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
                            <td colSpan="4">{title}</td>
                        </tr>
                        <tr className="units">
                            <td style={{textAlign: "center"}}><b>Number of units</b></td>
                            <td style={{textAlign: "center"}}><b>Cost per unit</b></td>
                            <td style={style}><b>{x_title}</b></td>
                        </tr>
                        {tableMap}
                        </tbody>
                    </table>
                </div>
            </div>
        )
    }
});


window.VouchersBasic = VouchersBasic;