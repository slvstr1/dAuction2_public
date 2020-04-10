
(function($)
{
    //    $(document).ready(function () {
    $(window).bind("load", function(){
        //refreshtime=20000;

        window_height=$(window).height();
        window_width=$(window).width()
        console.log("window_height",window_height);
        console.log("window_width",window_width);

        $('#Cancel').click
        (function () {
                var $my_standing_offer = $('#my_standing_offer');
                $my_standing_offer.load('/forward_and_spot/cancel_so/');
            }
        );


        $('#theoretical_predictions_button').click
        (function () {
                $.get( '/forward_and_spot/show_theory/', function (data) {});
            }
        );

        $('#stop_button').click
        (function () {
                $.get( '/forward_and_spot/stop/', function (data) {});
            }
        );

        $('#btnSell').click
        (function () {
                var valUnits = $('#unitsInput').val();
                var valPrice = $('#priceInput').val();
                var valType = 'SELL';
                //var $c24 = $('#c24');
                //var $container2 = $('#c14');
                var $my_standing_offer = $('#my_standing_offer');
                $my_standing_offer.load( '/forward_and_spot/set_offer/' + valUnits + '/' + valPrice + '/' + valType);
            }
        );


        $('#btnBuy').click
        (function () {
                var valUnits = $('#unitsInput').val();
                var valPrice = $('#priceInput').val();
                var valType = 'BUY';
                var $container3 = $('#my_standing_offer');
                $container3.load(  '/forward_and_spot/set_offer/' + valUnits + '/' + valPrice + '/' + valType);
                //$container.load('forward_and_spot/all_transactions/'+valUnits+'/'+valPrice);
            }
        );



//        var auto_refresh2 = setInterval
//        (
//            function () {
//                $.get('forward_and_spot/refresh2/', function (data) {});
//                $.get('forward_and_spot/refresh2/', function (data) {});

//            }
//            , 2000
//        );
        var auto_refresh = setInterval
        (
            function () {
                console.log('1111111111111111111111111111111111111111111111111111111111111something');
                console.log('id_in_group',id_in_group);

                $.get
                ('forward_and_spot/refresh/', function (data) {
                        var $all_transactions_digital = $(data).filter('#all_transactions_digital').html();
                        //var $my_cleared_offers = $(data).filter('#my_cleared_offers').html();
                        var $all_transactions = $(data).filter('#all_transactions').html();
                        var $all_transactions_text = $(data).filter('#all_transactions_text').html();
                        var $theoretical_predictions = $(data).filter('#theoretical_predictions').html();
                        var $theoretical_predictions_text = $(data).filter('#theoretical_predictions_text').html();
                        var $all_standing_market_offers = $(data).filter('#all_standing_market_offers').html();
                        var $my_standing_offer = $(data).filter('#my_standing_offer').html();
                        var $my_vouchers = $(data).filter('#my_vouchers').html();
                        //console.log('1111111111111111111111111111111111111111111111111111111111111something');
                        //console.log($my_cleared_offers);
                        $('#all_transactions_digital').html($all_transactions_digital);
                        //$('#my_cleared_offers').html($my_cleared_offers);
                        $('#all_transactions').html($all_transactions);
                        $('#all_transactions_text').html($all_transactions_text);
                        $('#theoretical_predictions_text').html($theoretical_predictions_text);
                        $('#theoretical_predictions').html($theoretical_predictions);
                        $('#all_standing_market_offers').html($all_standing_market_offers);
                        //$('#my_standing_offer').html($my_standing_offer);
                        //$('#my_vouchers').html($my_vouchers);
                    }
                );
            }
            , 5000
        );
    })
}(jQuery));
