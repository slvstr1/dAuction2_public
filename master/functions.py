import logging
from django.db.models import Func
from forward_and_spot.models import Player, Timer,  Player_stats, Auction, Treatment
from django.core.cache import cache
from .models import MasterMan


log = logging.getLogger(__name__)

class Round(Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 2)'


def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def set_treatment_main(request):
    id=int(request.POST['treatment'])
    Treatment.objects.all().update(active=False)
    treatment=Treatment.objects.get(id=id)
    log.info('id:{}'.format(id))
    log.info('treatment:{}'.format( treatment))
    treatment.active=True
    treatment.save_and_cache()

def get_options(treatment,auction,tt):

    # log.info("auction.distribution_auction_created:{}".format(auction.distribution_auction_created))
    options_set_state_request = {
        'set_treatment': set_treatment_main
    }

    # using caching resets the auction object somehow!!!
    # possible solutions: https://stackoverflow.com/questions/7936572/python-call-a-function-from-string-name
    # options_set_state_treatment = cache.get("options_set_state_treatment")
    # if not options_set_state_treatment:

    # ToDo: use name='' value='' in the form, where the name gives indication for the sort of action that might be done. name will select action, value gives parameter for that action (as in master_man.boolean_toggle
    options_set_state_treatment = {
        'auction_ready': auction.auction_ready,
        'summ_instructions_start': auction.summ_instructions_start_main,
        'demand_draws_create': auction.demand_draws_create_main,
        'full_instructions_start': auction.full_instructions_start_main,
        'distribution_start': auction.distribution_start,
        'testing_start': auction.testing_start,
        'auction_create': auction.auction_create_main,
        'auction_start': auction.auction_start,
        'shedding': auction.make_shedding,
        'random_together': auction.make_random_together,
    }
        # MasterMan.cache_it("options_set_state_treatment", options_set_state_treatment)

    # options_set_state = {
    #
    #                              }

    # options_set_state = cache.get("options_set_state")
    # if not options_set_state:
    master_man = MasterMan.cache_or_create_mm()
    options_set_state = {
        'refresh_all_players': Player.refresh_all_players,
        'invalidate_caches': MasterMan.invalidate_caches,
        'toggle_eductional': treatment.toggle_eductional,
        'toggle_no_test': master_man.toggle_no_test,
        'toggle_ip_login': master_man.toggle_ip_login,
        'flush_last_p_memory': master_man.flush_last_p_memory,
        'remove_userless_players': auction.remove_userless_players,
        'reset_players': auction.reset_players,
        # 'logging_requirement_overrule': log.info("pass8"),
        'demand_draws_delete': auction.demand_draws_delete,
        'instructions_cancel': auction.instructions_cancel,
        'distribution_cancel': auction.distribution_cancel,
        'testing_cancel': auction.testing_cancel,
        'testing_delete': auction.testing_delete,
        'auction_abort': auction.auction_abort,
        'auction_clear': auction.auction_clear,
        'timer_cut': tt.timer_cut,
        'timer_toggle': tt.timer_toggle,
        'timer_restart': timer_restart_main,
        'questionnaire_start': auction.questionnaire_start,
        'questionnaire_cancel': auction.questionnaire_cancel,
        'payout_start': auction.payout_start,
        'payout_cancel': auction.payout_cancel,
        'unstuck_all_in_payout': auction.unstuck_all_in_payout,
        'create_group': auction.create_group_main,
        'automatic_login_toggle': treatment.automatic_login_toggle,
        'only_spot_toggle': treatment.only_spot_toggle,
        'pay_one_random_period_toggle': treatment.pay_one_random_period_toggle,
        'allow_multiple_offers': treatment.allow_multiple_offers_toggle,
        'test_mode': treatment.test_mode_toggle,
        'make_instruction_pdf': auction.make_instruction_pdf_func,
        'show_ids': auction.show_ids_toggle,
        'test_players': treatment.set_test_players,
        'test_script': treatment.set_test_script,
        'delete_playerstats': auction.delete_playerstats_main,
        'removing': auction.make_removing,
        'unremoving': auction.make_unremoving,
        'kill_removed': auction.make_kill_removed,
        'revive_removed': auction.revive_removed,
        'strongest_together': auction.make_strongest_together,
        "delete": auction.auction_delete,
        'playerstats_create': Player_stats.playerStats_create,
        'logout_all': auction.make_logout_all}
        # MasterMan.cache_it("options_set_state", options_set_state)
    # log.info("auction.distribution_auction_created:{}".format(auction.distribution_auction_created))
    return options_set_state_request, options_set_state_treatment,options_set_state
        # ,options_set_state_auction


def  timer_restart_main():
    auction, treatment = Auction.cache_or_create_auction()
    tt = Timer.cache_get()
    tt=tt.timer_set(treatment.time_for_testing)
    tt.cache_me()
    auction.app_testing_started=True
    auction.app_testing_ended=False
    auction.save_and_cache()


def timer_toggle_main():
    tt = Timer.cache_get()
    tt.timer_toggle()
    tt.save_and_cache()
    log.info('timer_toggle()')