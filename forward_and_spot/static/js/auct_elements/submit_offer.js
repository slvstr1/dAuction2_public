// Form for offers and used functions
// needs   auction={this.state.auction}
//                     player_stats={this.state.player_stats}
//          player_id={this.state.player_id}
//          user_id={this.state.user_id}
//          auction_id={this.state.auction_id}
//          group_id={this.state.group_id}

var Submit_offer = React.createClass({
    getInitialState: function () {
        return {units: '', price: '', 'type': '', error: [], succes: [], re_status: [], re_data: []};
    },
    handleUnitChange: function (e) {
        this.setState({units: e.target.value});
    },
    handlePriceChange: function (e) {
        this.setState({price: e.target.value});
    },
    handleTypeChange: function (e) {
        if (e.target.value == "SELL") {
            var offer_type = 0;
        } else {
            var offer_type = 1;
        }
        this.setState({type: offer_type});
    },
    handleSubmit: function (e) {
        e.preventDefault();
        var unitsO = parseInt(this.state.units);
        var priceO = parseInt(this.state.price);
        var type = this.state.type;
        var contract = {
            "unitsOriginal": unitsO,
            "priceOriginal": priceO,
            "Type": type,
            "auction_id": this.props.auction_id,
            "user_id": this.props.user_id,
            "player_id": this.props.player_id,
            "group_id": this.props.group_id
        };
        // if both price and quantity are present, send offer to the server
        if (priceO && unitsO) {
            $.ajax({
                type: "POST",
                url: "/forward_and_spot/forward_and_spot/set_offer/",
                data: contract,
                success: function (data, status) {
                    this.setState({
                        re_data: data,
                        re_status: status
                    });
                    // empty the form
                    this.setState({price: '', units: '', type: ''});
                    // return statuses based on server
                    /// succes in posting
                    if (this.state.re_status == "nocontent") {
                        this.setState({succes: "Offer posted!"});
                        setTimeout(function () {
                            this.setState({succes: []});
                        }.bind(this), 1500);
                        // if success, there is an error
                    } else if (this.state.re_status == "success") {
                        this.setState({error: this.state.re_data[1]});
                        setTimeout(function () {
                            this.setState({error: []});
                        }.bind(this), 3500);
                    }
                }.bind(this)
            });
            // if Q or P are not present, log.info error
        } else {
            if (priceO) {
                this.setState({error: "There is no quantity specified!"});
                setTimeout(function () {
                    this.setState({error: []});
                }.bind(this), 3000);
            }
            if (unitsO) {
                this.setState({error: "There is no price specified!"});
                setTimeout(function () {
                    this.setState({error: []});
                }.bind(this), 3000);
            }
        }
    },
    render: function () {
        return (
            <div id="set_offer">
                <div className="title">Submit an offer</div>
                <form onSubmit={this.handleSubmit}>
                    <table>
                        <thead></thead>
                        <tbody>

                            <tr>
                                <td>Quantity:</td>

                                <td>
                                    <input
                                    type="number"
                                    max="999"
                                    min="1"
                                    step="1"
                                    width="50"
                                    placeholder="Quantity..."
                                    value={this.state.units}
                                    onChange={this.handleUnitChange}
                                    style={{height: "120%", width: "120%"}}
                                />
                                </td>
                            </tr>

                        <tr>
                            <td>Price:</td>
                            <td>
                                <input
                                    type="number"
                                    max="999"
                                    min="1"
                                    step="1"
                                    size="12"
                                    placeholder="Price..."
                                    value={this.state.price}
                                    onChange={this.handlePriceChange}
                                    style={{height: "120%", width: "120%"}}
                                />
                            </td>
                        </tr>


                        </tbody>
                    </table>
                    <div style={{margin: "5px 5px 5px 5px"}}>
                        <input type="submit" className="btnSell" value="SELL" onClick={this.handleTypeChange}/>
                        <input type="submit" className="btnBuy" value="BUY" onClick={this.handleTypeChange}/>
                        <div style={{color: "red"}}><b>{this.state.error}</b></div>
                        <div style={{color: "blue"}}><b>{this.state.succes}</b></div>

                    </div>
                </form>
            </div>
        );
    }
});

window.Submit_offer = Submit_offer;