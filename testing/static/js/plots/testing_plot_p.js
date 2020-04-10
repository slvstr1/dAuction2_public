// PLOT FOR TESTING
// NEEDS PLOTLY AND HIDDEN AUCTION FIELDS, DRAWS TO 'testingPlot
function arrayMin(arr) {
    var len = arr.length, min = Infinity;
    while (len--) {
        if (Number(arr[len]) < min) {
            min = Number(arr[len]);
        }
    }
    return min;
};
function arrayMax(arr) {
    var len = arr.length, max = -Infinity;
    while (len--) {
        if (Number(arr[len]) > max) {
            max = Number(arr[len]);
        }
    }
    return max;
};
function roundTen(value) {
    return Math.round(value / 10) * 10
}

function roundToNearest(numToRound, numToRoundTo) {
    return Math.round(numToRound / numToRoundTo) * numToRoundTo;
}

function standardDeviation(values) {
    var avg = average(values);
    var squareDiffs = values.map(function (value) {
        var diff = value - avg;
        var sqrDiff = diff * diff;
        return sqrDiff;
    });
    var avgSquareDiff = average(squareDiffs);
    var stdDev = Math.sqrt(avgSquareDiff);
    return stdDev;
}
function average(data) {
    var sum = data.reduce(function (sum, value) {
        return sum + value;
    }, 0);
    var avg = sum / data.length;
    return avg;
}

// params
var auction_d = (($('#auction_js').text()).replace(/\'/g, '\"')).replace(/\False/g, '0').replace(/\True/g, '1');
var vouchers_d = (($('#vouchers_js').text()).replace(/\'/g, '\"')).replace(/\False/g, '0').replace(/\True/g, '1');
var auction = $.parseJSON(auction_d);
var vouchers = $.parseJSON(vouchers_d);

//console.log(auction, vouchers);
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
// generate values
    var var_x = [mu, sigma];
    var var_y = [1 / (mu - sigma), 1 / (mu - sigma)];
// transformation
    var a = auction.a;
    var convex_para = auction.convexity_parameter;
    var pr_per_group = auction.PR_per_group;
    // needs to be generated, no PDF known
// generate X random draws and transform them
    var n_draws = 100000;
    var draws = [];
    for (i = 0; i <= n_draws; i++) {
        draws.push((a * Math.pow((Math.randomGaussian(mu, sigma)/ pr_per_group), (convex_para - 1))))
    }
    var price_mean = Math.round(average(draws));
    var price_std = Math.round(standardDeviation(draws));
    //console.log(a, sigma, mu, pr_per_group, convex_para);
// make histogram of them

// Y axis
    var x_min = sigma - sigma * 0.1;
    var x_max = mu + mu * 0.1;

// X axis
    var ymaxr = 1 / (mu - sigma) + 1 / (mu - sigma) * 0.1;
    var min_p = x_min * (1 - 0.025);
    var max_p = x_max * 1.025;
    var step = 5;
    var tick_max = 60
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

// plot
    var trace1 = {
        x: draws,

        type: 'histogram',
        histnorm: 'probability'
    };
    var data = [trace1];
    var layout = {
        marigin: (0, 0, 0, 0),
        xaxis: {
            range: [min_p, max_p], tickvals: label_array, tickmode: "array",
            title: "Price",
        },
        yaxis: {
            title: "Probability density",

        }
    };
}
if (distribution == "uniform") {
// generate values
    var var_x = [mu, sigma];
    var var_y = [1 / (mu - sigma), 1 / (mu - sigma)];
// transformation
    var a = auction.a;
    var convex_para = auction.convexity_parameter;
    var pr_per_group = auction.PR_per_group;
    // needs to be generated, no PDF known
// generate X random draws and transform them
    var n_draws = 100000;
    var draws = [];
    for (i = 0; i <= n_draws; i++) {
        draws.push((a * Math.pow((((Math.random()) * (sigma - mu) + mu) / pr_per_group), (convex_para - 1))))
    }
    var price_mean = Math.round(average(draws));
    var price_std = Math.round(standardDeviation(draws));
    var price_max = roundTen(arrayMax(draws));
    var price_min = roundTen(arrayMin(draws));
    //console.log(a, sigma, mu, pr_per_group, convex_para);
    var min_p = price_min*0.80;
    var max_p = price_max*1.15;
    var step = 5;
    var tick_max = 10
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

// make histogram of them

// Y axis
    var x_min = sigma - sigma * 0.1;
    var x_max = mu + mu * 0.1;

// X axis
    var ymaxr = 1 / (mu - sigma) + 1 / (mu - sigma) * 0.1;

// plot
    var trace1 = {
        x: draws,

        type: 'histogram',
        histnorm: 'probability'
    };
    var data = [trace1];
    var layout = {
        marigin: (0, 0, 0, 0),
        xaxis: {
            title: "Price",  range: [min_p, max_p], tickvals: label_array, tickmode: "array",

        },
        yaxis: {
            title: "Probability density",
            titlefont: {
                size: 18
            }

        }
    };
}
console.log(auction)
// plot to div "myDiv"
Plotly.newPlot('content1', data, layout, {staticPlot: true, displayModeBar: false});
$(document).ready(function () {
    $("#content2").append('<div style="width:100% !;"><p> The distribution of price has an average of ' + auction.price_avg_theory + ' with a standard deviation of ' + price_std + '.</p></div>');

})