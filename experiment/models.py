# import math
# import random
# import logging
# import os
# from django.db import models
#
#
#
#
# # from django.utils import timezone,
# from datetime import date
# from django.conf import settings
# from django.utils.encoding import python_2_unicode_compatible
# import datetime
# # from django import forms
# # from django.contrib.auth.models import AbstractUser
# # from django.contrib.auth import get_user_model
# # from django.utils.functional import cached_property
# # import time
# # from datetime import datetime
#
# log = logging.getLogger(__name__)
# # from master.functions_main import myround
# # from .managers import Extended_Manager, Extended_Manager_Auction,Extended_Manager_Player, ExtendedQuerySet
# # from master.functions_main import cache_me
# # from .managers import ExtendedQuerySet
# # from django.contrib.auth.models import UserManager
#
# # class Experiment(models.Model):
# #     created = models.DateTimeField(auto_now_add=True)
# #     description = models.CharField(max_length=125, default="auction, forward, Bessembinder and Lemmon (2002)")
# #
# # class BaseTreatment(models.Model):
# #     experiment = models.ForeignKey(Experiment, default=1,on_delete=models.CASCADE)
# #
# #     def __str__(self):
# #           # return "Auction {0} created on {1}".format(self.id, self.created)
# #           return "{0}".format(self.id)
# #
# #         # models.IntegerField(default= 8)
# #
#
#
# # class BasePlayer(models.Model):
# #     """ A player is one of the subjects. (S)he is a member of a group and has an id in the group.
# #     """
# #     WAIT = 1
# #     WORKING = 2
# #     FINISHED = 3
# #     VIEW_STATES = \
# #         (
# #             (WAIT, 'WAIT'),
# #             (WORKING, 'WORK'),
# #             (FINISHED, 'FIN'),
# #         )
# #
# #     NO=0
# #     INSTR = 1
# #     DISTR = 2
# #     TEST = 3
# #     FS = 4
# #     QUEST = 5
# #     PAYOUT=6
# #     VIEW_APPS = \
# #         (
# #             (NO, 'NONE'),
# #             (INSTR, 'INSTR'),
# #             (DISTR, 'DISTR'),
# #             (TEST, 'TEST'),
# #             (FS, 'FS'),
# #             (QUEST, 'QUEST'),
# #             (PAYOUT, 'PAYOUT'),
# #         )
# #     NOTNEEDREFRESHING=0
# #     NEEDREFRESHING = 1
# #     VIEW_PAGEREF = \
# #         (
# #             (NOTNEEDREFRESHING, 'NEED REFRESHING'),
# #             (NOTNEEDREFRESHING, 'OK'),
# #         )
# #     PR = 0
# #     RE = 1
# #
# #     ROLES = \
# #         (
# #             (PR, 'PR'),
# #             (RE, 'RE'),
# #         )
# #
# #     app = models.PositiveSmallIntegerField(choices=VIEW_APPS, default=NO)
# #     state = models.PositiveSmallIntegerField(choices=VIEW_STATES, default=WAIT)
# #     user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='player', on_delete=models.CASCADE,null=True, default=None)
# #     auction = models.ForeignKey(Auction, null=True,on_delete=models.CASCADE)
# #     group = models.ForeignKey(Group, null=True,on_delete=models.CASCADE)
# #     period=models.PositiveSmallIntegerField(default=1)
# #     page_need_refreshing = models.BooleanField(default=False)
# #     page= models.SmallIntegerField(default=1)
# #     test_page= models.PositiveSmallIntegerField(default=1)
# #     testing_finished= models.BooleanField(default=False)
# #     testing_trials = models.PositiveSmallIntegerField(default=0)
# #     testing_errors = models.PositiveSmallIntegerField(default=0)
# #     testing_correct = models.PositiveSmallIntegerField(default=0)
# #     selected = models.BooleanField(default=True)
# #     pageurl= models.CharField(max_length=165, default="")
# #     draw_id = models.PositiveSmallIntegerField(default=0)
# #     last_refresh_date = models.DateTimeField(default =date(2002, 12, 4))
# #     last_alive=models.SmallIntegerField(default=99)
# #     role = models.PositiveSmallIntegerField(choices=ROLES,default=PR)  # two roles: PRoducer and REtailer
# #     payout_ECU = models.IntegerField(default=0)
# #     payout_CZK = models.IntegerField(default=0)
# #     payout_qs = models.IntegerField(default=0)
# #     payout_trade = models.IntegerField(default=0)
# #     pay_period = models.PositiveSmallIntegerField(default=0)
# #     pay_qs_period =  models.PositiveSmallIntegerField(default=0)
# #     accuracy = models.FloatField(default=0)
# #     cumulative_earnings = models.FloatField(default=0)
# #     # the money earned by a player if the player (is positive if selling, negative if buying)
# #     total_cost = models.IntegerField(default=0)
# #     # the costs of production for a producer
# #     total_values = models.IntegerField(default=0)
# #     # the total of the values of the units a retailer purchased
# #     # profit = models.IntegerField(default=0)
# #     # net earnings of a player
# #     player_ready= models.BooleanField(default=False)
# #     earnings_CZK =models.IntegerField(default=0)
# #     earnings_CZK_corrected = models.IntegerField(default=0)
# #
# #     # Questionnaire elements
# #     first_name = models.CharField(max_length=224, default="")  # two roles: PRoducer and REtailer
# #     last_name = models.CharField(max_length=224, default="")  # two roles: PRoducer and REtailer
# #     male = models.BooleanField(default=True)
# #     age = models.PositiveSmallIntegerField(default=0)
# #     done_before= models.BooleanField(default=False)
# #     difficult_rating = models.PositiveSmallIntegerField(default=0)
# #     interesting_rating = models.PositiveSmallIntegerField(default=0)
# #     income_monthly_CZK = models.PositiveIntegerField(default=0)
# #     comments = models.TextField(default="")
# #     do_better_what = models.TextField(default="")
# #     time_spend_reading = models.PositiveSmallIntegerField(default=0)
# #     payout_CZK_corr = models.PositiveSmallIntegerField(default=0)
# #     # objects=Extended_Manager_Player()
# #     # objects = ExtendedQuerySet.as_manager()
# #
# #     # @property
# #     def get_payout_CZK_corr(self):
# #         if self.selected:
# #             if self.role==Player.PR:
# #                 return 10 * int(math.ceil(((self.payout_CZK + self.auction.fixed_uplift + self.auction.fixed_uplift_PR) * self.auction.multiplier * self.auction.multiplier_PR)/10))
# #             else:
# #                 return 10 * int(math.ceil(((
# #                    self.payout_CZK + self.auction.fixed_uplift + self.auction.fixed_uplift_RE) * self.auction.multiplier * self.auction.multiplier_RE)/10))
# #         else:
# #             return self.payout_CZK
# #
# #     # @property
# #     # def avg_paid_RE=
# #     # return sum(lt.cost for lt in self.lineitem_set)
# #
# #     def get_group_cache(self):
# #         pass
# #
# #     class Meta:
# #         ordering = ['pk']
# #     def __str__(self):
# #         return "id:{} gr:{}".format(self.id, self.group)
# #
# #     @property
# #     def ECU_per_CZK(self):
# #         treatment=self.auction.treatment
# #         if self.role == Player.PR:
# #             return treatment.ECU_per_CZK_PR
# #         else:
# #             return treatment.ECU_per_CZK_RE
# #     # def earnings_CZK(self):
# #     #     if self.role==Player.PR:
# #     #         return self.vouchers_used - self.vouchers_negative
# #
# #     def INSTR_app(self):
# #         self.app = Player.INSTR
# #         self.page = 1
# #         self.save()
# #
# #     def DISTR_app(self):
# #         self.app = Player.DISTR
# #         self.page = 0
# #         self.save()
# #
# #     def TEST_app(self):
# #         self.app = Player.TEST
# #         self.page = 1
# #         # self.save()
# #
# #     def FS_app(self):
# #         self.app = Player.FS
# #         self.page = 0
# #         self.save()
# #
# #     def QUEST_app(self):
# #         self.app = Player.QUEST
# #         self.page = 0
# #         self.save()
# #
# #     def PAYOUT_app(self):
# #         self.app = Player.PAYOUT
# #         self.page = 0
# #         self.save()
# #
# #     def get_pay_period(self, last_round_idd):
# #         log.info("old round for pay_period: {}".format(self.pay_period))
# #         # print("old round for pay_period: {}".format(self.pay_period))
# #         if last_round_idd==1:
# #             r=[1,]
# #             log.info("r=[1,]:{}".format(r))
# #             # print("r=[1,]:{}".format(r))
# #         else:
# #             log.info("self.pay_qs_period:{}".format(self.pay_qs_period))
# #             # print("self.pay_qs_period:{}".format(self.pay_qs_period))
# #             # print("last_round_idd:{}".format(last_round_idd))
# #
# #             r = list(range(1, self.pay_qs_period + 1)) + list(range(self.pay_qs_period + 1, last_round_idd + 1))
# #         log.info("new round for pay_period: {}".format(r))
# #         # print("new round for pay_period: {}".format(r))
# #         return random.choice(r)
# #
# #     def get_pay_qs_period(self, last_round_idd,treatment_qp_every):
# #         log.info("old round for pay_qs_period: {}".format(self.pay_qs_period))
# #         r=1 + (treatment_qp_every * (random.randint(0, int((last_round_idd / treatment_qp_every) - .001))))
# #         log.info("new round for pay_period: {}".format(r))
# #         return r
#
#     @property
#     def hardcoded_pics(self):
#         src_file02b = "/staticfiles/images/instructions_fig_02b_{}_{}_{}.png".format(self.distribution_used,self.uniform_min,self.uniform_max)
#         src_file18 = "/staticfiles/images/instructions_fig_18_{}_{}_{}.png".format(self.distribution_used,self.uniform_min,self.uniform_max)
#         src_file19 = "/staticfiles/images/instructions_fig_19_{}_{}_{}.png".format(self.distribution_used,self.uniform_min,self.uniform_max)
#         print("src_file02b:{}".format(src_file02b))
#         # cache.set('src_file02b', src_file02b)
#         # cache.set('src_file18', src_file18)
#         # cache.set('src_file19', src_file19)
#
#         src_file02b_exists = os.path.isfile(src_file02b[1:])
#         src_file18_exists = os.path.isfile(src_file18[1:])
#         src_file19_exists = os.path.isfile(src_file19[1:])
#         log.info("src_file02b_exists:{}, name:{}".format(src_file02b_exists, src_file02b))
#         log.info("src_file18_exists:{}, name:{}".format(src_file18_exists, src_file18))
#         log.info("src_file19_exists:{}, name:{}".format(src_file19_exists, src_file19))
#
#         src_file_exists = src_file02b_exists and src_file18_exists and src_file19_exists
#         a= [src_file02b, src_file18, src_file19]
#         return src_file_exists, a