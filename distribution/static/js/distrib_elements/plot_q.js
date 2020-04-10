/// Plot helper object for Quantity
function roundToNearest(numToRound, numToRoundTo) {
    return Math.round(numToRound / numToRoundTo) * numToRoundTo;
}

var RP1 = React.createClass({
    propTypes: {
        handle: React.PropTypes.string.isRequired,
        data: React.PropTypes.array.isRequired,
        layout: React.PropTypes.object
    },
    componentDidMount: function componentDidMount() {
        this.plot(this.props);
    },
    componentWillReceiveProps: function (nextProps) {
        this.plot(nextProps);
    },
    plot: function plot(props) {
        var handle = props.handle,
            data = props.data,
            layout = props.layout;
        return (
            Plotly.plot(handle, data, layout, {staticPlot: true, displayModeBar: false}));
    },
    render() {
        return React.createElement('helper', {id: this.props.handle}, "");
    }
});
// Demand plot
var Dist_plot1 = React.createClass({
    render () {
        var data_f = this.props.data;
        // main supply
        var trace2 = {
            x: this.props.data1,
            type: 'histogram',
            name: "Distribution",
            autobinx: false,
            histnorm: "probability density",
            xbins: {start: 0, end: this.props.demand_max, size: this.props.bar_width_q},
            marker: {color: 'red'},
        };
        var trace3 = {
            x: this.props.data2,
            type: 'histogram',
            name: "Random draw",
            autobinx: false,
            histnorm: "probability density",
            xbins: {start: 0, end: this.props.demand_max, size: this.props.bar_width_q},
            marker: {color: 'black'},
        };
        var min_d = this.props.demand_min*(1-0.025);
        var max_d = this.props.demand_max*1.025;
        var step = 5;
        var tick_max = 20
        var start = roundToNearest(min_d, step);
        var end = roundToNearest(max_d, step);
        var iter = (end-start)/step;
        while (iter > tick_max) {
            if (step == 5) {
                var step = 10
            }
            else {
                var step = step + 10;
            }
            var iter = (end-start)/step;
        }
        console.log(start, end)
        console.log(min_d, max_d)
        var label_array = []
        var i;
        for (i = 0; i <= iter; i++) {
         var tt = start + i*step;

         label_array.push(start + i*step)
        }
        console.log(label_array);
        if (max_d == 0) {
            var max_d = this.props.demand_max
        }
        var layout = {
            margin: {
                r: 35,
                b: 35,
                l: 70,
                t: 35
            },
              yaxis: {
                    title: 'probability density',
                    titlefont: {
                        size: 18
                    }
                },
            xaxis: {range: [min_d, max_d], tickvals: label_array, tickmode: "array"},
            autosize: false,
            width: 700,
            height: 400,
            showlegend: false,
            barmode: "overlay",
            title: 'Numerical simulation of the distribution <br> of the MARKET UNITS DEMANDED',
        };
        var data1 = [trace2, trace3];
        //Plotly.newPlot('myDiv', data1, layout);
        return (
            <div id="testeeeee">
                <RP1 id="plot" handle="plot" data={data1} layout={layout} key={this.props.timestamp} ref="plot"/>
            </div>
        );
    }
});

window.Dist_plot1 = Dist_plot1;
window.RP1 = RP1;

