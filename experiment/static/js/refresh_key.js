// simple snipplet to bind F5 to refresh the page (when kiosk mode is used)
$(document).keydown(function(e) {
    if(e.which == 116) {
        alert("keypress-reload");
      location.reload();
    }