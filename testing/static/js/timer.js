// React script for the timer
var Test_timer = React.createClass({
    // set init. state to empty
    getInitialState: function () {
        return {
            data_timer: {seconds_left: 0},
        };
    },
    fetchData: function () {
        $.get("/api/get_timer", function (data) {
            if (this.isMounted()) {
                this.setState({
                    data_timer: data.timer,
                });
            }
        }.bind(this));
    },
    componentDidMount: function () {
        this.fetchData();
        setInterval(function () {
            this.fetchData();
        }.bind(this), 1000);
    },
    render: function () {
        // logic
        var minutes = Math.floor(this.state.data_timer.seconds_left / 60)
        var seconds = (this.state.data_timer.seconds_left - minutes * 60)
        // enforce X X format
        function numDigits(x) {
            return (Math.log10((x ^ (x >> 31)) - (x >> 31)) | 0) + 1;
        }
        if (numDigits(seconds) < 2) {
            var d_seconds = "0" + seconds
        } else {
            var d_seconds = seconds
        }
        // display
        /// none if timer is -1
        if (this.state.data_timer.seconds_left >= 0) {
            var Display =   <div style={{display: 'flex', justifyContent: 'center'}}>  Time remaining: {minutes}:{d_seconds} </div>
        } else {
            var Display = <div></div>
        }
        return (
            < div  style={{
                                 textAlign: "left",
                                 position: "fixed",
                                 top: "0%",
                                 bottom: "90%",
                                 left: "20%",
                                 right: "20%",
                                 justifyContent: "center",
                                 alignItems: "center",

                             }}> {Display} </div >
        )
    }
});
ReactDOM.render(< Test_timer/>, document.getElementById("Timer"));