
import logging
from django.db import models
# from dAuction2.models import BaseMethods
# from django.core.cache import cache
from dAuction2.models import BaseMasterMan

log = logging.getLogger(__name__)
class MasterMan(BaseMasterMan):
    PARAMETERS = 1
    DATA = 3
    SHOW_EARNINGS = 5
    ANL = 4
    SANL = 6

    SUMMARY_INSTR = 0
    FULL_INSTR = 1

    ITYPES = (
        (SUMMARY_INSTR, 'SUMMARY INSTRUCTIONS'),
        (FULL_INSTR, 'FULL INSTRUCTIONS'),
    )
    WAIT = 0
    INSTR = 1
    DISTR = 2
    TESTING = 3
    FS = 4
    QUEST = 5
    PAYOUT = 6

    SHOW_ALL = 0
    SHOW_SELECTED_ONLY=1
    SHOW_UNSELECTED_ONLY = 2

    SHOW_TYPES = (
        (SHOW_ALL, 'Show ALL'),
        (SHOW_SELECTED_ONLY, 'Show SELECTED only'),
        (SHOW_UNSELECTED_ONLY, 'Show UNSELECTED only'),
    )


    APPTYPES = (
        (WAIT, 'WAITING'),
        (INSTR, 'INSTRUCTIONS'),
        (DISTR, 'DISTRIBUTION'),
        (TESTING, 'TESTING'),
        (FS, 'FORWARDANDSPOT'),
        (QUEST, 'QUESTIONNAIRE'),
        (PAYOUT, 'PAYOUT'),
    )

    MASTER_SCREEN_TYPES = (
        (PARAMETERS, 'PARAMETERS '),
        (DATA, 'DATA'),
        (SHOW_EARNINGS, 'SHOW_EARNINGS'),
        (ANL, 'ANL'),
        (SANL, 'SANL'),
    )
    ip_login = models.BooleanField(default=True)
    show_table = models.BooleanField(default=True)
    show_receipt_message = models.BooleanField(default=True)
    show_payments = models.BooleanField(default=False)
    view = models.PositiveSmallIntegerField(choices=MASTER_SCREEN_TYPES, default=PARAMETERS)
    pay_assistant = models.BooleanField(default=False)
    no_test = models.BooleanField(default=True)
    payment_sheet = models.BooleanField(default=False)
    show_selection = models.SmallIntegerField(default=0)

    # show_selected = models.BooleanField(default=True)
    show_unselected = models.BooleanField(default=True) # ToDo: can go!


    def boolean_toggle(self, property_string ):
        present_value = getattr(self, property_string, False)
        setattr(self, property_string, not present_value)
        self.save_and_cache()


    def get_property_from_request_POST(self, request_POST, html_function_name):
        # ToDO: bad thing is that this is a uber-hard coupling of html and code. So the value in the button must be the property of the MasterMan object. I can make a list here with the coupling.
        html_string = request_POST[html_function_name]
        property_string = html_string
        return property_string

    # ToDo: even better: in html is name=toggle, value= ... and then i match it here to an action.
    def toggler(self,request_POST):
        if 'boolean_toggle' in request_POST:
            property_string = self.get_property_from_request_POST(request_POST,html_function_name='boolean_toggle')
            # property_string = request_POST['boolean_toggle']
            if property_string:
                # print("using_boolean_toggle!!!")
                self.boolean_toggle(property_string)
        if 'boolean_toggle_refresh' in request_POST:
            # property_string = request_POST['boolean_toggle_refresh']
            property_string = self.get_property_from_request_POST(request_POST,html_function_name='boolean_toggle_refresh')
            if property_string:
                from forward_and_spot.models import Player
                # print("using_boolean_toggle_refresh!!!")
                self.boolean_toggle(property_string)
                Player.refresh_all_players(only_selected=True)

    def toggle_ip_login(self):
        from master.models import MasterMan
        self.ip_login = not self.ip_login
        self.save_and_cache()

    def flush_last_p_memory(self):
        from master.models import MasterMan
        from forward_and_spot.models import User
        User.objects.all().update(last_player=None)


    @classmethod
    def refresh_all_connected(cls):
        from forward_and_spot.models import Player
        Player.refresh_all_players()

    def get_selection(self, auction, isnull=True):
        from forward_and_spot.models import Player
        # print("in_get_selection")
        player_list = Player.objects.filter(auction=auction).order_by('-selected',  'user_id','user__ip', 'group_id')
        if self.show_selection == MasterMan.SHOW_ALL:
            player_list = Player.objects.filter(auction=auction).order_by('-selected',  'user_id', 'user__ip', 'group_id')
        elif self.show_selection == MasterMan.SHOW_SELECTED_ONLY:
            player_list = Player.objects.filter(auction=auction, selected=True).order_by('user_id','user__ip', 'group_id')
        elif self.show_selection == MasterMan.SHOW_UNSELECTED_ONLY:
            player_list = Player.objects.filter(auction=auction, selected=False).order_by('-selected', 'user_id', 'user__ip','group_id')

        # print("show_selection:{}".format(self.show_selection))
        # print("player_list:{}".format(player_list))
        return player_list


    def show_selection_toggle(self):
        self.show_selection = (self.show_selection +1)%3
        # print("new_show_selection_toggle:{}".format(self.show_selection))
        self.save_and_cache()


from dAuction2.models import BaseMethods
class Assistant(BaseMethods):

    def __init__(self, first_name="", last_name = "", id_or_birth_number="", target_payment=500,earning = 0):

        # payment_range = 100
        self.first_name=first_name
        self.last_name =last_name
        self.id_or_birth_number =id_or_birth_number
        self.target_payment = target_payment
        self.earning = earning