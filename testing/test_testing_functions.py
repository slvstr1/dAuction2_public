import json
from django.core.cache import cache
from django.test import TestCase, RequestFactory
from forward_and_spot.models import Offer, Auction, Player,  Group, Player_stats, Period, Phase, Timer, Treatment
from testing.models import Option_MC,Question
# from dAuction2.models import Experiment
from dAuction2.models import User
from forward_and_spot.models import MasterMan
from distribution.models import Distribution
# from .functions import define_questions
# from master.functions_main import  cache_me, invalidate_caches

import time

# from django.http import *


class test_define_questions(TestCase):
    def setUp(self):
        print("**********************")
        print("setUp")
        print("**********************")


    def tearDown(self):
        # Clean up run after every test method.
        from forward_and_spot.models import Voucher
        from distribution.models import Distribution
        MasterMan.invalidate_caches()
        Offer.objects.all().delete()
        Player.objects.all().delete()
        Player_stats.objects.all().delete()
        Auction.objects.all().delete()
        Period.objects.all().delete()
        Phase.objects.all().delete()
        Group.objects.all().delete()
        Voucher.objects.all().delete()
        Timer.objects.all().delete()
        Distribution.objects.all().delete()
        User.objects.all().delete()
        Treatment.objects.all().delete()
        print("**********************")
        print("tearDown --- DELETED")
        print("**********************")

    def test_define_questions(self):
        auction,treatment = Auction.cache_or_create_auction()
        # treatment.save
        # auction = Auction.create()
        # auction.save
        Option_MC.objects.all().delete()
        Question.objects.all().delete()

        auction.testing_totalquestions = Question.define_questions(treatment,auction)

        option_list= Option_MC.objects.all().select_related('question')
        n_option = option_list.count()
        # print("n_option:",n_option)
        self.assertEqual(n_option, 85)
        # print("option_list:",option_list)
        # for option in option_list:
        #     print(option.question_id," ",option.id," ",option.explanation_text)

        question_list = Question.objects.all()
        n_question = question_list.count()
        # print("n_question:", n_question)

        assert (n_question == 19)

        for question in question_list:
            print(question.id," ",question.question_text)

        # assert (False)



