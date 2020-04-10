import logging, math
from forward_and_spot.models import Player_stats,Period

log = logging.getLogger(__name__)


def determine_payment(treatment, auction, player):
    last_round = Period.objects.filter(auction=auction, finished=True).order_by('id').last()
    log.info("determine_payment")
    # print("determine_payment")
    if not last_round:
        log.info("finished round object does not exist")
        # last_round = Period.objects.filter(auction=auction).order_by('id').last() - useless...
    else:
        log.info("last_round:{}".format(last_round))

        if treatment.pay_one_random_period:
            if player.pay_qs_period > last_round.idd:
                player.pay_qs_period = player.get_pay_qs_period(last_round.idd, treatment.qp_every)
                log.info("player:{}".format(player))
                log.info("auction:{}".format(auction))
                log.info("player.pay_qs_period:{}".format(player.pay_qs_period))
                # print("player.pay_qs_period:{}".format(player.pay_qs_period))
                period = Period.objects.get(idd=player.pay_qs_period)
                player_stats = Player_stats.objects.get(player=player,auction=auction,period= period)
                player.payout_qs = player_stats.profit_accuracy
                player.save()
            if player.pay_period > last_round.idd:
                player.pay_period = player.get_pay_period(last_round.idd, player.pay_qs_period)
                period = Period.objects.get(idd=player.pay_qs_period)
                player_stats = Player_stats.objects.get(player=player, auction=auction, period=period)
                player.payout_trade = player_stats.profit
                log.info("new round for pay_period: {}".format(player.pay_period ))
                player.save()
            player.payout_ECU = player.payout_qs + player.payout_trade
        else:
            player.payout_ECU = player.cumulative_earnings/last_round.idd

        player.earnings_CZK = player.payout_ECU / player.ECU_per_CZK
        player.payout_CZK = max(0,10 * int((math.ceil(player.earnings_CZK) + treatment.start_capital_in_CZK + treatment.showupfee_fixed)/10))
        player.payout_CZK_corr = player.payout_CZK
        player.accuracy = player.payout_qs
        player.save()


def auction_pay_removed(request, treatment, auction, player):
    # log.info('i5')
    # print("player.testing_finished:{}".format(player.testing_finished))

    if not player.testing_finished:
        player.payout_CZK = treatment.showupfee_desel_error_max
        message = "You were not selected for the continuation of the experiment. As you did not finish the test, you will be paid the small show-up fee of {} CZK".format(
            player.payout_CZK)
        log.info("message:{}".format(message))
    elif player.testing_errors > treatment.error_max:
        player.payout_CZK = treatment.showupfee_desel_error_max
        message = "You were not selected for the continuation of the experiment. As you made {} mistakes, which is more than {}, you will be paid the small show-up fee of {} CZK".format(
            player.testing_errors, treatment.error_max, player.payout_CZK)
    else:
        player.payout_CZK = treatment.showupfee_desel
        message = "You were not selected for the continuation of the experiment. You will be paid the show-up fee of {} CZK".format(
            player.payout_CZK)

    after_message = "Please move quietly outside of the lab, where one of the experimenters will pay you your earnings"
    player.save()
    data = {}
    group_id = player.group_id
    data.update({"treatment": treatment, 'player': player, 'group_id': group_id, "auction": auction, "message": message,"after_message": after_message})
    log.info("data: {}".format(data))
    return data