// PLOT FOR TESTING
// NEEDS PLOTLY AND HIDDEN AUCTION FIELDS, DRAWS TO 'testingPlot
function roundToNearest(numToRound, numToRoundTo) {
    return Math.round(numToRound / numToRoundTo) * numToRoundTo;
}

// params
// params
var auction_d = (($('#auction_js').text()).replace(/\'/g, '\"')).replace(/\False/g, '0').replace(/\True/g, '1');
var vouchers_d = (($('#vouchers_js').text()).replace(/\'/g, '\"')).replace(/\False/g, '0').replace(/\True/g, '1');
var auction = $.parseJSON(auction_d);
var vouchers = $.parseJSON(vouchers_d);
// normal
if (auction.distribution_used == 1) {
    var mu = auction.mu;
    var sigma = auction.sigma;
    var distribution = "normal";
} else {
    var mu = auction.uniform_max;
    var sigma = auction.uniform_min;
    var distribution = "uniform";
}

if (distribution == "normal") {
// computation
    var x_min = Math.max(0, mu - 4 * sigma);
    var x_max = mu + 4 * sigma;
    var normal_x = []
    var normal_y = []

    for (i = x_min; i <= x_max; i++) {
        var first = (1 / ( Math.sqrt(2 * Math.pow(sigma, 2) * 3.14159)));
        var exp = -((Math.pow(i - mu, 2)) / (2 * Math.pow(sigma, 2)));
        var value = first * Math.pow(2.71828, exp);
        normal_x.push(i);
        normal_y.push(value);
    }
    var xticks = [mu, mu + sigma, mu + 2 * sigma, mu + 3 * sigma, mu + 4 * sigma]
    for (i = 1; i <= 4; i++) {
        if ((mu - i * sigma) > 0.1) {
            xticks.unshift(mu - i * sigma)
        }
    }
// Y
    var ymax = Math.max.apply(Math, normal_y);
    var ymaxr = Math.round(ymax * 1000) / 1000;
    var yticks = [0, ymaxr]
    var distance = ymax / 4;
    for (i = 1; i <= 3; i++) {
        yticks.unshift(Math.round(distance * i * 1000) / 1000)

    }
    var trace1 = {
        x: normal_x,
        y: normal_y,
        fill: 'tozeroy',
        type: 'scatter',
        tickmode: 'array',
    };
    var data = [trace1];
    var layout = {

        xaxis: {
            range: [x_min, x_max],
            tickvals: xticks,
            autorange: false,
            title: "Number of MARKET UNITS DEMANDED",
        },
        yaxis: {
            range: [0, ymaxr],
            tickvals: yticks,
            autorange: false,
            tickformat: ".3f",
            title: "Probability density",

        }
    };
}
if (distribution == "uniform") {
// generate values
    var var_x = [mu, sigma];
    var var_y = [1 / (mu - sigma), 1 / (mu - sigma)];
// Y axis
    var x_min = sigma;
    var x_max = mu;
    var ymaxr = 1 / (mu - sigma) + 1 / (mu - sigma) * 0.1;
// X axis
    var distance = x_max - x_min;
    console.log("d", distance)
    if (distance > 20) {
         var min_p = x_min * 0.50;
    var max_p = x_max + (x_min- x_min * 0.50);
    } else {
         var min_p = x_min * 0.80;
    var max_p = x_max + (x_min- x_min * 0.80);
    }

    var step = 5;
    var tick_max = 12
    var start = roundToNearest(min_p, 10);
    var end = roundToNearest(max_p, 10);
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
    var middle = (sigma-mu)/2
    var label_array = [0,mu, sigma, middle]
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

// plot
    var trace1 = {
        x: var_x,
        y: var_y,
        fill: 'tozeroy',
        type: 'scatter',
        tickmode: 'array',
    };
    var data = [trace1];
    var layout = {

        xaxis: {
                    range: [min_p, max_p], tickvals: label_array, tickmode: "array", title: "Number of MARKET UNITS DEMANDED",
                },

        yaxis: {
            range: [0, ymaxr],
            autorange: false,
            tickformat: ".3f",
            title: 'probability density',
            titlefont: {
                size: 18
            }


        }
    };
}

// plot to div "myDiv"
Plotly.newPlot('content1', data, layout, {staticPlot: true, displayModeBar: false});
