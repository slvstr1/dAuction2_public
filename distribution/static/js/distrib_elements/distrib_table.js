// Tables
var Table_row = React.createClass({
    render: function () {
        return (<tr>
                <td>{this.props.idd}</td>
                <td>{this.props.demand_draw}</td>
                <td>{this.props.price_draw}</td>
            </tr>
        )
    }
});
var Distrib_table = React.createClass({
    render: function () {
        var distrib1_copy = JSON.parse(JSON.stringify(this.props.distrib1));
        var distrib2_copy = JSON.parse(JSON.stringify(this.props.distrib2));
        //  for (var key in distrib1_copy) {
        //             if (distrib1_copy.hasOwnProperty(key)) {
        //                 distrib1_copy[key].demand_draw = Math.round(distrib1_copy[key].demand_draw*10)/10;
        //                distrib1_copy[key].price_draw = Math.round(distrib1_copy[key].price_draw*10)/10;
        //             }
        //  }
        // for (var key in distrib2_copy) {
        //             if (distrib2_copy.hasOwnProperty(key)) {
        //                 distrib2_copy[key].demand_draw = Math.round(distrib2_copy*10)/10;
        //                 distrib2_copy[key].price_draw = Math.round(distrib2_copy[key].price_draw*10)/10;
        //             }
        //  }
        var distrib1 = distrib1_copy.map(function (i) {
            return (
                <Table_row key={i.id} idd={i.idd} demand_draw={i.demand_draw} price_draw={i.price_draw}></Table_row>)
        });
        var distrib2 = distrib2_copy.map(function (i) {
            return (
                <Table_row key={i.id} idd={i.idd} demand_draw={i.demand_draw} price_draw={i.price_draw}></Table_row>)
        });
        return (
            <div>
                <div className="col-lg-3">          {/*<!-- ROW 2, COLUMN 1 -->*/}
                    <div style={{height: 650}}>
                        <table style={{width: 300, fontSize: "11", marginLeft: 5}}
                               className="table table-striped  table-condensed">
                            <thead style={{color: "#fff", backgroundColor: "#373a3c"}}>
                            <tr>
                                <td><b>Draw #</b></td>
                                <td><b>Demand</b></td>
                                <td><b>Lowest Possible Price</b></td>
                            </tr>
                            </thead>
                            <tbody>
                            {distrib1}
                            </tbody>
                        </table>
                    </div>
                </div>
                <div className="col-lg-3">          {/* <!-- ROW 2, COLUMN 2 -->*/}
                    <table style={{width: 300, fontSize: "11"}} className="table table-striped  table-condensed">
                        <thead style={{color: "#fff", backgroundColor: "#373a3c"}}>
                        <tr>
                            <td><b>Draw #</b></td>
                            <td><b>Demand</b></td>
                            <td><b>Lowest Possible Price</b></td>
                        </tr>
                        </thead>
                        <tbody>
                        {distrib2}
                        </tbody>
                    </table>
                </div>
            </div>
        )
    }
});

window.Distrib_table = Distrib_table