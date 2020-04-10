import serpy
from rest_framework import serializers
from forward_and_spot.models import Auction, Treatment, Group, Offer, Player, Player_stats,Phase, Period


class sPenaltySerializer(serpy.Serializer):
    id = serpy.Field()
    phase_id = serpy.Field()
    player_stats_id = serpy.Field()
    amounth = serpy.Field()


class sTimerSerializer(serpy.Serializer):
    """The serializer schema definition."""
    # Use a Field subclass like IntField if you need more validation.
    # end = serpy.BoolField
    running = serpy.BoolField()
    # waiting_page = serpy.BoolField()
    seconds_left = serpy.IntField()
    short_seconds_left = serpy.IntField()


class sTreatmentSerializer(serpy.Serializer):
    max_vouchers = serpy.IntField()
    short_maximum = serpy.IntField()
    mu = serpy.FloatField()
    sigma = serpy.FloatField()
    a = serpy.FloatField()
    PR_per_group = serpy.IntField()
    convexity_parameter = serpy.IntField()
    d_draws_needed = serpy.IntField()
    retail_price = serpy.FloatField()
    # app_forward_and_spot=serpy.BoolField()
    # app=serpy.IntField()
    # auction_started=serpy.BoolField()
    # time_refresh_data=serpy.IntField()
    # end=serpy.BoolField()
    uniform_max = serpy.IntField()
    uniform_min = serpy.IntField()
    time_conditional = serpy.IntField()
    penalty_perunit = serpy.IntField()
    # show_ids = serpy.BoolField()
    price_avg_theory = serpy.FloatField()
    # created= serpy.StrField()
    distribution_used = serpy.IntField()
    time_refresh_check = serpy.IntField()
    educational = serpy.BoolField()
    only_spot = serpy.BoolField()
    require_units_demanded_on_PR = serpy.BoolField()

class sAuctionSerializer(serpy.Serializer):
    # app_forward_and_spot=serpy.BoolField()
    app = serpy.IntField()
    auction_started = serpy.BoolField()
    time_refresh_data = serpy.IntField()
    end = serpy.BoolField()
    show_ids = serpy.BoolField()
    created = serpy.StrField()


class sUserSerializer(serpy.Serializer):
    state = serpy.StrField()
    logged_in = serpy.BoolField()
    # has_player= serpy.BoolField()
    fail = serpy.BoolField()
    last_refresh_date = serpy.Field()
    # last_alive=serpy.Field()
    ip = serpy.StrField()
    username = serpy.StrField()


class sPlayerNestedSerializer(serpy.Serializer):
    user = sUserSerializer()
    # group = serpy.Field()
    id = serpy.Field()
    # ip = serpy.StrField()

    # testing_errors = serpy.Field()
    testing_correct = serpy.Field()
    testing_errors = serpy.Field()
    app = serpy.Field()
    state = serpy.Field()
    page = serpy.Field()
    # last_refresh_date = serpy.Field()
    last_alive = serpy.Field()
    role = serpy.Field()
    player_ready = serpy.Field()
    auction_id = serpy.Field()
    group_id = serpy.IntField()
    user_id = serpy.Field()
    page_need_refreshing = serpy.Field()
    selected = serpy.Field()


class sPlayerSerializer(serpy.Serializer):
    # user = sUserSerializer()
    # group = serpy.Field()
    id = serpy.Field()
    # testing_errors = serpy.Field()
    testing_correct = serpy.Field()
    testing_errors = serpy.Field()
    app = serpy.Field()
    state = serpy.Field()
    page = serpy.Field()
    # last_refresh_date = serpy.Field()
    # last_alive = serpy.Field()
    role = serpy.Field()
    player_ready = serpy.Field()
    auction_id = serpy.Field()
    group_id = serpy.IntField()
    user_id = serpy.Field()
    selected = serpy.Field()


class sPhaseSerializer(serpy.Serializer):
    idd = serpy.Field()
    waiting_page = serpy.Field()
    question_page = serpy.Field()
    active_state = serpy.Field()
    # nothing = serpy.Field()
    # period_id = serpy.Field()


class sPeriodSerializer(serpy.Serializer):
    idd = serpy.Field()


class sPlayer_statsSerializer(serpy.Serializer):
    id = serpy.Field()
    period_id = serpy.Field()
    profit = serpy.Field()
    # player_demand = serpy.Field()
    end_penalty = serpy.Field()
    trading_result = serpy.Field()
    trading_result_stage1 = serpy.Field()
    total_values = serpy.Field()
    vouchers_negative = serpy.Field()
    vouchers_used = serpy.Field()
    vouchers_negative_stage1 = serpy.Field()
    vouchers_used_stage1 = serpy.Field()
    # this can clearly be optimized! (sPlayer_stats_invarSerializer)
    role = serpy.Field()
    total_cost = serpy.Field()
    units_missing = serpy.Field()
    penalty_phase_total = serpy.Field()

class sPlayer_statsSerializer_with(sPlayer_statsSerializer):
    player_demand = serpy.Field()




class sVSerializer(serpy.Serializer):
    id = serpy.Field()
    idd = serpy.Field()
    # value_cum = serpy.Field()
    value = serpy.Field()
    auction_id = serpy.Field()


class sOfferSerializer(serpy.Serializer):
    id = serpy.Field()
    offer_tiepe = serpy.Field()
    unitsAvailable = serpy.Field()
    priceOriginal = serpy.Field()
    cleared = serpy.Field()
    unitsCleared = serpy.Field()
    priceCleared = serpy.Field()
    player_id = serpy.Field()
    # unitsOriginal = serpy.Field()
    product = serpy.Field()
    # role = serpy.Field()


class sPlayerDrawSerializer(serpy.Serializer):
    id = serpy.Field()
    draw_id = serpy.Field()


# class sDistribSerializer(serializers.ModelSerializer):
class sDistribSerializer(serpy.Serializer):
    id = serpy.Field()
    idd = serpy.Field()
    demand_draw = serpy.Field()
    price_draw = serpy.Field()
    test = serpy.Field()
    auction_id = serpy.Field()


# class pOfferSerializer(serpy.Serializer):
#     id = serpy.Field()
#     offer_tiepe = serpy.Field()
#     unitsAvailable = serpy.Field()
#     priceOriginal = serpy.Field()
#     cleared = serpy.Field()
#     unitsCleared = serpy.Field()
#     priceCleared = serpy.Field()
#     player_id = serpy.Field()
#     # unitsOriginal = serpy.Field()
#     product = serpy.Field()
#     # role = serpy.Field()
#     created = serpy.StrField()
#     timeCleared = serpy.StrField()
#     canceled = serpy.Field()
#     phase_id = serpy.Field()


# class pPhaseSerializer(serpy.Serializer):
#     idd = serpy.Field()
#     id = serpy.Field()
#     waiting_page = serpy.Field()
#     question_page = serpy.Field()
#     active_state = serpy.Field()
#     created = serpy.StrField()
#     end = serpy.StrField()
#     period_id = serpy.Field()


# class pPeriodSerializer(serpy.Serializer):
#     idd = serpy.Field()
#     id = serpy.Field()
#     updated = serpy.StrField()
#     # total_demand = serpy.Field()





# put ANL in its own app?
# complete serializers used for data transfers to ANL app
# class AnlOfferSer(serializers.ModelSerializer):
#     class Meta:
#         model = Offer
#         fields = "__all__"
#
#
# class AnlPeriodSer(serializers.ModelSerializer):
#     class Meta:
#         model = Period
#         fields = "__all__"
#
#
# class AnlPhaseSer(serializers.ModelSerializer):
#     class Meta:
#         model = Phase
#         fields = "__all__"
#
#
# class AnlPlayerSer(serializers.ModelSerializer):
#     class Meta:
#         model = Player
#         fields = "__all__"
#
#
# class AnlTreatmentSer(serializers.ModelSerializer):
#     class Meta:
#         model = Treatment
#         fields = "__all__"
#
# class AnlAuctionSer(serializers.ModelSerializer):
#     class Meta:
#         model = Auction
#         fields = "__all__"
#
# class AnlPlayerStatsSer(serializers.ModelSerializer):
#     class Meta:
#         model = Player_stats
#         fields = "__all__"
#
# class AnlGroupStatsSer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = "__all__"
