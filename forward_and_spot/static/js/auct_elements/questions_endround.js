/// Question between rounds modal and used functions

var Questions_endround = React.createClass({
    getInitialState: function () {
        return {a1: '', a2: '', a3: '', w_show: 0, answered: 0};
    },
    handleA1Change: function (e) {
        this.setState({a1: e.target.value});
    },
    handleA2Change: function (e) {
        this.setState({a2: e.target.value});
    },
    handleA3Change: function (e) {
        this.setState({a3: e.target.value});
    },
    handleButtonEnable: function (e) {
        var a1 = this.state.a1;
        var a2 = this.state.a2;
        var a3 = this.state.a3;
        if (a1 && a2 && a3) {
            this.setState({d_button: 1});
        }
        ;
    },
    handleSubmit: function (e) {
        e.preventDefault();
        var a1 = this.state.a1;
        var a2 = this.state.a2;
        var a3 = this.state.a3;
        var answers = {"a1": a1, "a2": a2, "a3": a3};
        if (a1 && a2 && a3) {
            $.ajax({
                type: "POST",
                url: "/api/round_questions/",
                data: answers,
            });
            this.setState({a1: '', a2: '', a3: '', w_show: 0, answered: 1});
        } else {
            console.log("ANSWER FAILED");
            this.setState({w_show: 1});
        }
    },
    render: function () {
        // logic for submited states
        if (this.state.w_show == 0) {
            var warning = <div></div>
        } else {
            var warning = <div><strong>Please fill-out all the answers!</strong></div>
        }
        if (this.state.answered == 0) {
            var Button = <input style={{marginTop: 10}} className="btn btn-primary" type="submit" value="Submit"
                                onClick={this.handleSubmit}/>
        } else {
            var Button = <div><strong>Your answer has been noted. Thank you!</strong></div>
        }
        // stage framing with educational settings
        if (this.props.educational == false) {
            var stage2_framing = <span>Stage 2</span>
            var name_framing = <span>experiment</span>
        } else {
            var stage2_framing = <span>the Spot Market</span>
            var name_framing = <span>Business Game</span>
        }
        return (
            <div>
                <center>
                    <table style={{padding: 10}}>
                        <thead>
                        </thead>
                        <tbody>

                        <form onSubmit={this.handleSubmit}>

                            <tr style={{padding: 5}}>
                                <td><h3><strong>1. What is your estimate of the average of the MARKET UNITS DEMANDED in {stage2_framing} of the coming round?</strong></h3>
                                </td>
                            </tr>
                            <tr>
                                <td style={{padding: 5}}>
                                    <input
                                        type="number"
                                        max="999"
                                        min="1"
                                        step="1"
                                        size="12"
                                        required={true}
                                        value={this.state.a1}
                                        onChange={this.handleA1Change}
                                    /></td>
                            </tr>
                            <tr style={{padding: 5}}>
                                <td><h3><strong>2. What is your estimate of the average of prices in {stage2_framing} of the
                                    coming round?</strong></h3>
                                </td>
                            </tr>
                            <tr>
                                <td style={{padding: 5}}>
                                    <input
                                        type="number"
                                        max="999"
                                        min="1"
                                        step="1"
                                        width="50"
                                        required={true}
                                        value={this.state.a2}
                                        onChange={this.handleA2Change}
                                    /></td>
                            </tr>
                            <tr style={{padding: 10}}>
                                <td><h3><strong>3. What is your estimate of what the average of prices would be in {stage2_framing} of the
                                    coming round if competition was perfect?</strong></h3>
                                </td>
                            </tr>
                            <tr>
                                <td style={{padding: 5}}>
                                    <input
                                        type="number"
                                        max="999"
                                        min="1"
                                        step="1"
                                        width="50"
                                        required={true}
                                        value={this.state.a3}
                                        onChange={this.handleA3Change}/></td>
                            </tr>

                        </form>
                        <tr></tr>
                        <tr>
                            <td>
                                {Button}
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <tr>
                                    <td>
                                        {warning}
                                    </td>
                                </tr>
                                {warning}
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <br/>
                                <h3>You will be rewarded according to your accuracy. Your answer will not be communicated to the other participants in the {name_framing}.</h3>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </center>
            </div>
        );
    }
});

window.Questions_endround = Questions_endround;