/// Plot helper object for Price
function roundToNearest(numToRound, numToRoundTo) {
    return Math.round(numToRound / numToRoundTo) * numToRoundTo;
}

var RP2 = React.createClass({
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
var Dist_plot2 = React.createClass({
    render () {
        var data_f = this.props.data;
        // main supply
        var trace2 = {
            x: this.props.data1,
            type: 'histogram',
            name: "Distribution",
            autobinx: false,
            histnorm: "probability density",
            xbins: {start: 0, end: this.props.price_max, size: this.props.bar_width_p},
            marker: {color: 'red'},
        };
        var trace3 = {
            x: this.props.data2,
            type: 'histogram',
            name: "Random draw",
            autobinx: false,
            histnorm: "probability density",
            xbins: {start: 0, end: this.props.price_max, size: this.props.bar_width_p},
            marker: {color: 'black'},
        };
        var min_p = this.props.price_min * (1 - 0.025);
        var max_p = this.props.price_max * 1.025;
        var step = 5;
        var tick_max = 20
        var start = roundToNearest(min_p, step);
        var end = roundToNearest(max_p, step);
        var iter = (end - start) / step;
        while (iter > tick_max) {
            if (step == 5) {
                var step = 10
            }
            else {
                var step = step + 10;
            }
            var iter = (end - start) / step;
        }
        console.log(start, end)
        console.log(min_p, max_p)
        var label_array = []
        var i;
        for (i = 0; i <= iter; i++) {
            var tt = start + i * step;
            console.log(tt);
            label_array.push(start + i * step)
        }
        console.log(label_array)
        if (max_p == 0) {
            var max_p = this.props.price_max
        }
        var layout = {
                margin: {
                    r: 35,
                    b: 35,
                    l: 70,
                    t: 35
                },
                xaxis: {
                    range: [min_p, max_p], tickvals: label_array, tickmode: "array"
                },
                yaxis: {
                    title: 'probability density',
                    titlefont: {
                        size: 18
                    }
                },
                autosize: false,
                width: 700,
                height: 400,
                showlegend: false,
                barmode: "overlay",
                title: 'Numerical simulation of the distribution <br>of the Lowest Possible Price',
            }
            ;
        var data1 = [trace2, trace3];
        //Plotly.newPlot('myDiv', data1, layout);
        return (
            <div id="testeeeee">
                <RP2 id="plot" handle="plot2" data={data1} layout={layout} key={this.props.timestamp} ref="plot"/>
            </div>
        );
    }
});


window.Dist_plot2 = Dist_plot2;
window.RP1 = RP2;
