/// History table
/// displays history table, contains AJAX call with check for new data, if period ID changes
/// needs:
// player_id={
// this.state.player_id}
// user_id={this.state.user_id}
// auction_id={this.state.auction_id}
// group_id={this.state.group_id}
// period.idd
// history={this.state.history} - inside depends on role, see row objects
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
function parseID(str) {
  let to_string = str.toString();
  let last_4_digits = to_string.substring(to_string.length-4, to_string.length);
   // console.log("parseID:", to_string, last_4_digits, parseInt(last_4_digits));
  return  parseInt(last_4_digits);

};
var Navbar = ReactBootstrap.Navbar,
    Nav = ReactBootstrap.Nav,
    NavItem = ReactBootstrap.NavItem,
    NavDropdown = ReactBootstrap.NavDropdown,
    MenuItem = ReactBootstrap.MenuItem,
    Modal = ReactBootstrap.Modal,
    Button = ReactBootstrap.Button;

var History_rowRE = React.createClass ({
    render: function () {
        return (<tr style={{textAlign: "center"}}>
                <td style={{textAlign: "right", width:"4%"}}>{this.props.idd}</td>
                <td style={{textAlign: "right", width: "16%"}} >{this.props.profit}</td>
                <td style={{textAlign: "right", width: "16%"}}>{this.props.player_demand}</td>
                <td style={{textAlign: "right", width: "16%"}}>{this.props.units_obtained}</td>
                <td style={{textAlign: "right", width: "16%"}}>{this.props.penalty}</td>
                <td style={{textAlign: "right", width: "16%"}}>{this.props.total_values}</td>
                <td style={{textAlign: "right", width: "16%"}}>{this.props.trading_result}</td>
            </tr>
        )
        }
});
var History_rowPR = React.createClass ({
    render: function () {
        return (<tr>
                <td style={{textAlign: "right",width: "4%"}}>{this.props.idd}</td>
                <td style={{textAlign: "right",width: "16%"}}>{this.props.profit}</td>
                 <td style={{textAlign: "right",width: "16%"}}>{this.props.player_demand}</td>
                 <td style={{textAlign: "right",width: "16%"}}>{this.props.units_obtained}</td>
                 <td style={{textAlign: "right",width: "16%"}}>{this.props.penalty}</td>
                <td style={{textAlign: "right",width: "16%"}}>{this.props.total_cost}</td>
                <td style={{textAlign: "right",width: "16%"}}>{this.props.trading_result}</td>
            </tr>
        )
        }
});
var HistoryTable = React.createClass ({
 getInitialState: function () {
        return {
         history: []
        };
    },
    fetchHistoryDataC: function () {
      // feches history data and saves then to state, called at render by main object and every period change here
        $.ajax({
        type: "POST",
        url: "/api/history_data",
        data: {
          'auction_id': this.props.auction_id,
          'user_id': this.props.user_id,
          'player_id': this.props.player_id,
          'group_id': this.props.group_id
        },
        success: function(data,status){
          // phase
         var history = data.history;
         this.setState({
            history: history,
        });
      }.bind(this)})
  },
  componentWillMount: function() {
      // fire AJAX if period changes
    //  if (this.props.period.idd != nextProps.period.idd) {
          this.fetchHistoryDataC();
     // } else {
          //console.log("Nope!");
      //}
  },
  // history table logic
  // Retailer
  render(){
  if (this.props.player_stats.role==1) {
      // swith between props and state, history is loaded in render to props, after period change to state
      if (this.props.history.length > this.state.history.length) {
          var tomap = this.props.history;
      } else {
          var tomap = this.state.history;
      }
      var tomap_copy = JSON.parse(JSON.stringify(tomap));
      tomap_copy.sort(sort_by("period_id", false, parseID));
      // add round
      for (var key in tomap_copy) {
          if (tomap_copy.hasOwnProperty(key)) {
              tomap_copy[key].round = parseInt(key) + 1;
              tomap_copy[key].units_obtained = tomap_copy[key].vouchers_used - tomap_copy[key].vouchers_negative
          }
      }
      var Map_history = tomap_copy.map(function (contract) {
          return ( <History_rowRE
              key={contract.id}
              idd={contract.round}
              period={contract.period_id}
              profit={contract.profit}
              player_demand={contract.player_demand}
              penalty={contract.penalty_phase_total}
              trading_result={contract.trading_result}
              units_obtained={contract.units_obtained}
              total_values={contract.total_values}>
          </History_rowRE>)
      });
      var table_head = <tr style={{textAlign: "right"}}>
          <td style={{textAlign: "right", width: "4%"}}><b>Round</b></td>
          <td style={{textAlign: "right", width: "16%"}}><b>Profit</b></td>
          <td style={{textAlign: "right", width: "16%"}}><b>UNITS DEMANDED</b></td>
          <td style={{textAlign: "right", width: "16%"}}><b>Units obtained</b></td>
          <td style={{textAlign: "right", width: "16%"}}><b>Penalty</b></td>
          <td style={{textAlign: "right", width: "16%"}}><b>Earnings</b></td>
          <td style={{textAlign: "right", width: "16%"}}><b>Trading Revenue</b></td>
      </tr>;
   } else {
   // Producer history table
      if (this.props.history.length > this.state.history.length) {
          var tomap = this.props.history;
      } else {
          var tomap = this.state.history;
      }
      var tomap_copy = JSON.parse(JSON.stringify(tomap));
      tomap_copy.sort(sort_by("period_id", false, parseID));
      // add round
      for (var key in tomap_copy) {
          if (tomap_copy.hasOwnProperty(key)) {
              tomap_copy[key].round = parseInt(key) + 1;
              tomap_copy[key].units_obtained = tomap_copy[key].vouchers_used - tomap_copy[key].vouchers_negative
          }
      }
      var Map_history = tomap_copy.map(function (contract) {
          return ( <History_rowPR
              key={contract.id}
              idd={contract.round}
              profit={contract.profit}
              player_demand={contract.player_demand}
              units_obtained={contract.units_obtained}
              penalty={contract.penalty_phase_total}
              total_cost={contract.total_cost}
              trading_result={contract.trading_result}>
          </History_rowPR>)
      });
      if (this.props.pr_no_UD == false) {
          var table_head = <tr style={{textAlign: "right"}}>
              <td style={{textAlign: "right", width: "4%"}}><b>Round</b></td>
              <td style={{textAlign: "right", width: "16%"}}><b>Profit</b></td>
              <td style={{textAlign: "right", width: "16%"}}><b>UNITS DEMANDED</b></td>
              <td style={{textAlign: "right", width: "16%"}}><b>Units sold</b></td>
              <td style={{textAlign: "right", width: "16%"}}><b>Penalty</b></td>
              <td style={{textAlign: "right", width: "16%"}}><b>Total cost</b></td>
              <td style={{textAlign: "right", width: "16%"}}><b>Trading Revenue</b></td>
          </tr>;
      } else {
          var table_head = <tr style={{textAlign: "right"}}>
              <td style={{textAlign: "right", width: "4%"}}><b>Round</b></td>
              <td style={{textAlign: "right", width: "16%"}}><b>Profit</b></td>
              <td style={{textAlign: "right", width: "16%"}}><b>UNITS DEMANDED</b></td>
              <td style={{textAlign: "right", width: "16%"}}><b>Units sold</b></td>
              <td style={{textAlign: "right", width: "16%"}}><b>Penalty</b></td>
              <td style={{textAlign: "right", width: "16%"}}><b>Total cost</b></td>
              <td style={{textAlign: "right", width: "16%"}}><b>Trading Revenue</b></td>
          </tr>;
      }
   }
    return(

    <div>
        <Modal.Body bsClass="modal">
            <div
                style={{
                    height: "300",
                    top: 0,
                    bottom: 0,
                    right: 0,
                    left: 0,
                    margin: "5px 5px 5px 0px",
                    backgroundColor: "transparent"
                }}>
                <div className="title"
                     style={{marginTop: 30, backgroundColor: "whitesmoke", width: "98%", fontSize: "20"}}>History
                    table
                </div>
                <table style={{cellspacing: 0, cellpadding: 0, border: 0, width: "100%"}}>
                    <thead>
                    </thead>
                    <tbody>
                    <tr>
                        <td>
                            <table style={{
                                textAlign: "right",
                                cellspacing: 0,
                                cellpadding: 1,
                                border: "1px solid black",
                                width: "98%"
                            }}>
                                <thead>
                                {table_head}
                                </thead>
                                <tbody>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div style={{width: "100%", overflow: "auto", backgroundColor: "white"}}>
                                <table
                                    style={{
                                        textAlign: "right",
                                        cellspacing: 0,
                                        cellpadding: 1,
                                        border: "1px solid black",
                                        width: "98%"
                                    }}>
                                    <thead></thead>
                                    <tbody>
                                    {Map_history}
                                    </tbody>
                                </table>
                            </div>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </Modal.Body>
    </div>
      )}

});


window.HistoryTable = HistoryTable
