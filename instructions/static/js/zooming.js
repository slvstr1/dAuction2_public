// // new zooming
// // split settings of navbar, footer and content based on different resolutions
// // the same on all pages

var width = screen.width;
var height = screen.height;
console.log(width, height);
// navbar and footer not zooming
$("#i_footer").css({"zoom":"1"});
$("#i_navbar").css({"zoom":"1"});

// zooming of content depends on screen resolution (not viewport size!!)
//lab square
    if (width == 1280 && height == 1024) {
        var zoom_level = 0.75;
        var padding_rescale = String(Math.round(70*(1/zoom_level))) + "px";
        $("#i_content").css({"zoom": String(zoom_level)});
        $("#i_content").css({"padding-bottom": padding_rescale});
//lab normal
    } else if (width == 1680 && height == 1050) {
        var zoom_level = 0.75;
        var padding_rescale = String(Math.round(70*(1/zoom_level))) + "px";
        $("#i_content").css({"zoom": String(zoom_level)});
        $("#i_content").css({"padding-bottom": padding_rescale});
// lab special
    } else if (width == 1920 && height == 1080) {
        var zoom_level = 0.75;
        var padding_rescale = String(Math.round(70*(1/zoom_level))) + "px";
        $("#i_content").css({"zoom": String(zoom_level)});
        $("#i_content").css({"padding-bottom": padding_rescale});
// other - home
    } else {
        var zoom_level = 0.75;
        var padding_rescale = String(Math.round(70*(1/zoom_level))) + "px";
        $("#i_content").css({"zoom": String(zoom_level)});
        $("#i_content").css({"padding-bottom": padding_rescale});
    }

