// Master elements for the table

// SELL AND BUY offer standing transaction table
var Offer_master1 = React.createClass({
    render() {
        var sell_o_1 = [{'id': 1, 'p': 10, 'q': 5}, {'id': 2, 'p': 8, 'q': 1}, {'id': 3, 'p': 7, 'q': 2}, {
            'id': 4,
            'p': 6,
            'q': 1
        }];
        var buy_o_1 = [{'id': 1, 'p': 4, 'q': 2}, {'id': 2, 'p': 2, 'q': 1}];
        return (
            <div>
                <AllContractsTable n={1} sell_o={sell_o_1} buy_o={buy_o_1}/>
            </div>
        )
    }
});

ReactDOM.render(<Offer_master1/>, document.getElementById("content1"));

var Offer_master2 = React.createClass({
    render() {
        var sell_o_2 = {'id': 1, 'p': 1, 'q': 10};
        var buy_o_2 = {'id': 1, 'p': 1, 'q': 10};
        return (
            <div>
                <AllContractsTable n={2} sell_o={sell_o_2} buy_o={buy_o_2}/>
            </div>
        )
    }
});

ReactDOM.render(<Offer_master2/>, document.getElementById("content3"));