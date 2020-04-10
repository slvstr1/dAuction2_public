// MARKET INFO
// information about the market from server
// all_offers object - all offers on the market, cleared, uncleared, doesnt matter
/// calculates market charasteristics from them
// define sorting function
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

var MarketInfo = React.createClass({
	  render: function () {
      if (this.props.all_offers.length == 0) {
          var cleared_offers = [];
      } else {
          var offers_copy = JSON.parse(JSON.stringify(this.props.all_offers));
          var cleared_offers = $.grep(offers_copy, function (n, i) {
              return n.cleared == true;
          });
      }
      if (cleared_offers.length == 0) {
          var sum_10="";
          var sum_all = "";
          var sum_units = "";
          var median_10 = "";
          var median_all = "";
      } else {
          // calculate market info stats
          var cleared_offers = $.grep(this.props.all_offers, function (n, i) {
              return n.cleared == true;
          });
          // split list to last 10 transactions and all
          var max_id = Math.max.apply(Math, cleared_offers.map(function (o) {
              return o.id;
          }));
          var offers_10 = $.grep(cleared_offers, function (n, i) {
              return n.id >= max_id - 10;
          });
          // extract prices
          var prices_offers_10 = offers_10.map(function (o) {
              return o.priceCleared;
          });
          var prices_offers = cleared_offers.map(function (o) {
              return o.priceCleared;
          });
          // calculate mean and median
          if (cleared_offers.length == 1) {
              var avg_10 = prices_offers_10[0];
              var avg_all = prices_offers[0];
              var median_10 = avg_10;
              var median_all = avg_all;
          } else {
              let sum_10 = prices_offers_10.reduce((previous, current) => current += previous);
              var avg_10 = Math.round(sum_10 / prices_offers_10.length);
              let sum_all = prices_offers.reduce((previous, current) => current += previous);
              var avg_all = Math.round(sum_all / prices_offers.length);
              prices_offers_10.sort((a, b) => a - b);
              var median_10 = Math.round((prices_offers_10[(prices_offers_10.length - 1) >> 1] + prices_offers_10[prices_offers_10.length >> 1]) / 2);
              prices_offers.sort((a, b) => a - b);
              var median_all = Math.round((prices_offers[(prices_offers.length - 1) >> 1] + prices_offers[prices_offers.length >> 1]) / 2);
              // sum of all units
              var sum_units = cleared_offers.map(function (o) {
                  return o.unitsCleared;
              }).reduce(function (a, b) {
                  return a + b;
              }, 0);
          }
      }
          return (
              <div style={{margin: "0% 2% 2% 2%", position: "absolute", width: "100%", height: "100%"}}>
                  <div className="title" style={{}}>Market information</div>
                  <table style = {{width: "100%", height: "100%"}}>
                      <tbody>
                      <tr>
                          <td style = {{width: "40%"}}><strong>Price last 10 transactions
                              <div>(all transactions):</div>
                          </strong></td>
                          <td style = {{width: "40%"}}><strong>Units:</strong></td>
                      </tr>
                      <tr>

                          <td style = {{width: "40%"}}>
                              <li>Median price :{median_10}
                                  ({median_all})
                              </li>
                          </td>
                          <td style = {{width: "40%"}}>
                              <li>Units traded: {sum_units}</li>
                          </td>
                      </tr>
                      <tr>

                          <td style = {{width: "40%"}}>
                              <li>Average price: {avg_10}
                                  ({avg_all})
                              </li>
                          </td>
                      </tr>
                      <tr>
                          <td style = {{width: "40%"}}>&nbsp;</td>
                          <td style = {{width: "40%"}}>&nbsp;</td>
                      </tr>
                      </tbody>
                  </table>
              </div>
        );
	  }
	});

window.MarketInfo = MarketInfo;
