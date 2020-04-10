from django.db import models
from dAuction2.models import BaseMethods
from dAuction2.settings import UNIQUEIZER
from django.contrib.auth.models import User
from forward_and_spot.models import Auction, Treatment, Player
# should run from /home/vagrant/venv/bin/python
# run manage.py loaddata deployment/db_users.json
#from master.models import *
import logging, random

log = logging.getLogger(__name__)

############################################################################3
# testing models
#####################################################################

class Question(BaseMethods, models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, null=True,default=None,on_delete=models.CASCADE)
    question_text = models.TextField(default="")
    js = models.TextField(default="")
    js2 = models.BooleanField(default=False)
    url = models.SlugField(max_length=200,default="")
    pic_height = models.CharField(max_length=20,default="250")
    pic_width = models.CharField(max_length=20,default="500")

    @classmethod
    def get_totalquestions(cls, auction):
        # from testing.models import Question
        return cls.objects.filter(auction=auction).count()

    @classmethod
    def define_questions(cls, treatment, auction):
        def get_question(cls, treatment,auction,question_text, id,pic_width,pic_height,url,is_js, option_dict_list):
            question = cls(treatment=treatment, auction=auction,
                           question_text=question_text, id=id, pic_width=pic_width, pic_height=pic_height,
                           url=url, js2=is_js)

            question.save()
            to_insert_options = []
            for i, option_dict in enumerate(option_dict_list):
                option_mc = Option_MC(question=option_dict['question'], option_text=option_dict['option_text'], idd=i+1, correct=option_dict['correct'],
                                explanation_text=option_dict['explanation_text'])
                option_mc.save()
                # to_insert_options.extend([option_mc])



        to_insert_options = []
        to_insert_questions = []
        cls.objects.filter(treatment=treatment).delete()
        i = auction.id *UNIQUEIZER + 1
        if not treatment.only_spot:

            question = cls(treatment=treatment,auction=auction,
                                question_text="Given the distribution in the picture below, what is the probability that the MARKET UNITS DEMANDED is equal or larger than {0}?".format(
                                    treatment.get_average_uniform), id=i, pic_width=751, pic_height=419,
                                url="staticfiles/images/DR_M60_SD20.jpg", js2=True)
            # question.save()
            option1 = Option_MC(question=question, option_text="0%", idd=1, correct=False,
                                explanation_text="As you can see in the graph, it happens frequently that the number of required units is larger than {0}. Thus 0% cannot be correct.".format(
                                    treatment.get_average_uniform))
            option2 = Option_MC(question=question, option_text="25%", idd=2, correct=False,
                                explanation_text="As you can see in the graph, the area on the right of {0} is as large as the area to the left of {0}.".format(
                                    treatment.get_average_uniform))
            option3 = Option_MC(question=question, option_text="50%", idd=3, correct=True,
                                explanation_text="As you can see in the graph, the area on the right of {0} is as large as the area to the left of {0}. The probability of the number of required units being equal or larger than {0} is therefore 50%".format(
                                    treatment.get_average_uniform))
            option4 = Option_MC(question=question, option_text="75%", idd=4, correct=False,
                                explanation_text="As you can see in the graph, the area on the right of {0} is as large as the area to the left of {0}.".format(
                                    treatment.get_average_uniform))
            option5 = Option_MC(question=question, option_text="100%", idd=5, correct=False,
                                explanation_text="As you can see in the graph, it happens frequently that the number of required units is smaller than {0}. Thus 100% cannot be correct.".format(
                                    treatment.get_average_uniform))
            to_insert_questions.append(question)
            log.info(to_insert_questions)
            to_insert_options.extend([option1, option2, option3, option4, option5])


            # i=2
            i += 1
            question = cls(treatment=treatment,auction=auction,
                                question_text="When drawing the MARKET UNITS REQUIRED from the distribution below, what is the probability that an outcome between {0:10.2f} and {1:10.2f} is chosen?".format(
                                    (treatment.uniform_min + treatment.get_length_uniform / 4),
                                    (treatment.uniform_min + treatment.get_length_uniform * 3 / 4)), pic_width=751,
                                pic_height=419, url="staticfiles/images/DR_M60_SD20.jpg", id=i, js2=True)

            to_insert_questions.append(question)
            log.info(to_insert_questions)
            option1 = Option_MC(question=question, option_text="20%", idd=1, correct=False,
                                explanation_text="The probability mass of outcomes between {0:10.2f} and {1:10.2f} is more than 20% of the total probability mass.".format(
                                    (treatment.uniform_min + treatment.get_length_uniform / 4),
                                    (treatment.uniform_min + treatment.get_length_uniform * 3 / 4)))
            option2 = Option_MC(question=question, option_text="30%", idd=2, correct=False,
                                explanation_text="The probability mass of outcomes between {0:10.2f} and {1:10.2f} is more than 30% of the total probability mass.".format(
                                    (treatment.uniform_min + treatment.get_length_uniform / 4),
                                    (treatment.uniform_min + treatment.get_length_uniform * 3 / 4)))
            option3 = Option_MC(question=question, option_text="40%", idd=3, correct=False,
                                explanation_text="The probability mass of outcomes between {0:10.2f} and {1:10.2f} is more than 40% of the total probability mass.".format(
                                    (treatment.uniform_min + treatment.get_length_uniform / 4),
                                    (treatment.uniform_min + treatment.get_length_uniform * 3 / 4)))
            option4 = Option_MC(question=question, option_text="50%", idd=4, correct=True,
                                explanation_text="The probability mass of outcomes between {0:10.2f} and {1:10.2f} is half the probability mass of the all outcomes (between {2:10.2f} and {3:10.2f}). The probability of an outcome between {0:10.2f} and {1:10.2f} is thus indeed 50 %.".format(
                                    (treatment.uniform_min + treatment.get_length_uniform / 4),
                                    (treatment.uniform_min + treatment.get_length_uniform * 3 / 4), treatment.uniform_min,
                                    treatment.uniform_max))
            option5 = Option_MC(question=question, option_text="60%", idd=5, correct=False,
                                explanation_text="The probability mass of outcomes between {0:10.2f} and {1:10.2f} is less than 60% of the total probability mass.".format(
                                    (treatment.uniform_min + treatment.get_length_uniform / 4),
                                    (treatment.uniform_min + treatment.get_length_uniform * 3 / 4)))
            to_insert_options.extend([option1, option2, option3, option4, option5])

            # i=3
            i += 1
            question = cls(treatment=treatment,auction=auction,
                                question_text="What is the expected number of MARKET UNITS DEMANDED for the distribution below? In other words, what is the average of MARKET UNITS DEMANDED if we drew this number many times randomly from the distribution below?",
                                pic_width=751, pic_height=419, url="staticfiles/images/DR_M60_SD20.jpg", id=i, js2=True)
            to_insert_questions.append(question)
            log.info(to_insert_questions)

            option1 = Option_MC(question=question, option_text="{0:10.1f}".format(
                treatment.uniform_min + treatment.get_length_uniform * 1 / 5), idd=1, correct=False,
                                explanation_text="Look for the average value in the distribution.")
            option2 = Option_MC(question=question, option_text="{0:10.1f}".format(
                treatment.uniform_min + treatment.get_length_uniform * 5 / 6), idd=2, correct=False,
                                explanation_text="Look for the average value in the distribution.")
            option3 = Option_MC(question=question, option_text="{0:10.1f}".format(treatment.get_average_uniform), idd=3,
                                correct=True)
            option4 = Option_MC(question=question, option_text="{0:10.1f}".format(
                treatment.uniform_min + treatment.get_length_uniform * 1 / 3), idd=4, correct=False,
                                explanation_text="Look for the average value in the distribution.")
            option5 = Option_MC(question=question, option_text="{0:10.1f}".format(
                treatment.uniform_min + treatment.get_length_uniform * 2 / 3), idd=5, correct=False,
                                explanation_text="Look for the average value in the distribution.")
            to_insert_options.extend([option1, option2, option3, option4, option5])

            # i=4
            i += 1
            question = cls(treatment=treatment,auction=auction,
                                question_text="What is approximately (allowing for a possible rounding error) the expected price for the distribution of prices below? In other words, what is the average of prices if we drew them many times randomly from the distribution below?",
                                pic_width=751, pic_height=419, url="staticfiles/images/DR_M60_SD20.jpg", id=i, js2=True)
            # question.save()
            to_insert_questions.append(question)
            option1 = Option_MC(question=question, option_text=int(treatment.price_avg_theory * 0.2), idd=1, correct=False,
                                explanation_text="Look for the average value in the distribution.")
            option2 = Option_MC(question=question, option_text=int(treatment.price_avg_theory * 0.6), idd=2,
                                correct=False, )
            option3 = Option_MC(question=question, option_text=int(treatment.price_avg_theory), idd=3, correct=True)
            option4 = Option_MC(question=question, option_text=int(treatment.price_avg_theory * 1.4), idd=4, correct=False,
                                explanation_text="Look for the average value in the distribution.")
            to_insert_options.extend([option1, option2, option3, option4])

            # i=5
            i += 1
        question = cls(treatment=treatment,auction=auction,
                            question_text="Look at the Offer Overview in the picture below. Given the offers at this moment, what is the cheapest price for which you can buy 1 unit?",
                            id=i, pic_width=360, pic_height=440, url="staticfiles/images/testing01.png", js2=True)
        to_insert_questions.append(question)

        option1 = Option_MC(question=question, option_text="1", idd=1, correct=False,
                            explanation_text="As you want to buy, you need to look in the column with the SELL offers. As you can see, there are no SELL offers with a price of 1.")
        option2 = Option_MC(question=question, option_text="2", idd=2, correct=False,
                            explanation_text="As you want to buy, you need to look in the column with the SELL offers. As you can see, there are no SELL offers with a price of 2.")
        option3 = Option_MC(question=question, option_text="4", idd=3, correct=False,
                            explanation_text="As you want to buy, you need to look in the column with the SELL offers. As you can see, there are no SELL offers with a price of 4.")
        option4 = Option_MC(question=question, option_text="6", idd=4, correct=True,
                            explanation_text="As you want to buy, you need to look in the column with the SELL offers. As you can see, the cheapest offer is indeed for a price of 6.")
        option5 = Option_MC(question=question, option_text="7", idd=5, correct=False,
                            explanation_text="As you want to buy, you need to look in the column with the SELL offers. There are indeed two units on offer for a price of 7, but 7 is not the cheapest price among all SELL offers.")
        option6 = Option_MC(question=question, option_text="8", idd=6, correct=False,
                            explanation_text="As you want to buy, you need to look in the column with the SELL offers. There are indeed two units on offer for a price of 8, but 8 is not the cheapest price among all SELL offers.")

        to_insert_options.extend([option1, option2, option3, option4, option5, option6])


        # i=6
        i += 1
        question = cls(treatment=treatment,auction=auction,
                            question_text="Look at the Offer Overview in the picture below. Given the offers at this moment, what is the highest price for which you can sell 1 unit?",
                            id=i, pic_width=400, pic_height=500, url="staticfiles/images/testing01.png", js2=True)
        to_insert_questions.append(question)

        option1 = Option_MC(question=question, option_text="1", idd=1, correct=False,
                            explanation_text="As you want to sell, you need to look in the column with the BUY offers. There is indeed one units asked for a price of 1, but 1 is not the highest price among all BUY offers.")
        option2 = Option_MC(question=question, option_text="2", idd=2, correct=False,
                            explanation_text="As you want to sell, you need to look in the column with the BUY offers. There is indeed one units asked for a price of 2, but 2 is not the highest price among all BUY offers.")
        option3 = Option_MC(question=question, option_text="4", idd=3, correct=True,
                            explanation_text="As you want to sell, you need to look in the column with the BUY offers. As you can see, the most expensive BUY offer has indeed a price of 4.")
        v = "6"
        option4 = Option_MC(question=question, option_text=v, idd=4, correct=False,
                            explanation_text="As you want to sell, you need to look in the column with the BUY offers. As you can see, there are no BUY offers with a price of %s." % v)
        v = "7"
        option5 = Option_MC(question=question, option_text=v, idd=5, correct=False,
                            explanation_text="As you want to sell, you need to look in the column with the BUY offers. As you can see, there are no BUY offers with a price of %s." % v)
        v = "8"
        option6 = Option_MC(question=question, option_text=v, idd=6, correct=False,
                            explanation_text="As you want to sell, you need to look in the column with the BUY offers. As you can see, there are no BUY offers with a price of %s." % v)
        to_insert_options.extend([option1, option2, option3, option4, option5, option6])

        # i=7
        i += 1
        question = cls(treatment=treatment,auction=auction,
                            question_text="Look at the Offer Overview in the picture below. Given the offers at this moment, what is the cheapest price for which you can buy 1 unit?",
                            pic_width=400, pic_height=500,
                            id=i, url="staticfiles/images/testing02.png", js2=True)
        to_insert_questions.append(question)

        option1 = Option_MC(question=question, option_text="1", idd=1, correct=False,
                            explanation_text="As you want to buy, you need to look in the column with the SELL offers. As you can see, there are no SELL offers with a price of 1.")
        option2 = Option_MC(question=question, option_text="2", idd=2, correct=False,
                            explanation_text="As you want to buy, you need to look in the column with the SELL offers. As you can see, there are no SELL offers with a price of 2.")

        v = "4"
        option3 = Option_MC(question=question, option_text=v, idd=3, correct=True,
                            explanation_text="As you want to buy, you need to look in the column with the SELL offers. As you can see, the cheapest offer is indeed for a price of %s." % v)
        v = "5"
        option4 = Option_MC(question=question, option_text=v, idd=4, correct=False,
                            explanation_text="As you want to buy, you need to look in the column with the SELL offers. There are indeed two units on offer for a price of %s, but %s is not the cheapest price among all SELL offers." % (
                                v, v))
        to_insert_options.extend([option1, option2, option3, option4])

        # i=8
        i += 1
        question = cls(treatment=treatment,auction=auction,
                            question_text="Look at the Offer Overview in the picture below. Given the offers at this moment, what is the highest price for which you can sell 1 unit?",
                            pic_width=400, pic_height=500,
                            id=i, url="staticfiles/images/testing02.png", js2=True)
        to_insert_questions.append(question)
        v = "1"
        option1 = Option_MC(question=question, option_text=v, idd=1, correct=False,
                            explanation_text="As you want to sell, you need to look in the column with the BUY offers. There is indeed one units asked for a price of %s, but %s is not the highest price among all BUY offers." % (
                                v, v))
        v = "2"
        option2 = Option_MC(question=question, option_text=v, idd=2, correct=False,
                            explanation_text="As you want to sell, you need to look in the column with the BUY offers. As you can see, the most expensive BUY offer has indeed a price of %s." % v)
        v = "4"
        option3 = Option_MC(question=question, option_text=v, idd=3, correct=True,
                            explanation_text="As you want to sell, you need to look in the column with the BUY offers. As you can see, there are no BUY offers with a price of %s." % v)
        v = "5"
        option4 = Option_MC(question=question, option_text=v, idd=4, correct=False,
                            explanation_text="As you want to sell, you need to look in the column with the BUY offers. As you can see, there are no BUY offers with a price of %s." % v)
        to_insert_options.extend([option1, option2, option3, option4])

        # i=9
        i += 1
        question = cls(treatment=treatment,auction=auction,
                            question_text="Look at the Offer Overview in the picture below. Given the offers at this moment, if I submit a SELL offer of 3 units for a price of 1, how many units do I sell?",
                            id=i, url="staticfiles/images/testing02.png", pic_width=400, pic_height=500, js2=True)
        to_insert_questions.append(question)
        option1 = Option_MC(question=question, option_text="1 unit", idd=1, correct=False,
                            explanation_text="The price for which you make your SELL offer is equal or lower than all the three offers in the BUY column of the Offers Overview. Your SELL offer can thus be matched to more than 1 unit.")
        option2 = Option_MC(question=question, option_text="2 units", idd=2, correct=False,
                            explanation_text="The price for which you make your SELL offer is equal or lower than all the three offers in the BUY column of the Offers Overview. Your SELL offer can thus be matched to more than 2 units.")
        option3 = Option_MC(question=question, option_text="3 units", idd=3, correct=True,
                            url="staticfiles/images/testing02_ answer08.png", pic_width=300, pic_height=400,
                            explanation_text="The price for which you make your SELL offer is equal or lower than all the three offers in the BUY column of the Offers Overview. You thus indeed sell all your 3 units.")
        to_insert_options.extend([option1, option2, option3])

        # i=10
        i += 1
        question = cls(treatment=treatment,auction=auction,
                            question_text="Look at the Offer Overview in the picture below. Given the offers at this moment, we determined before that if I submit a SELL offer of 3 units for a price of 1, I will sell 3 units. For what price(s) will I sell these 3 units?",
                            id=i, url="staticfiles/images/testing02.png", pic_width=450, pic_height=500, js2=True)

        to_insert_questions.append(question)
        option1 = Option_MC(question=question, option_text="for a price of 1", idd=1, correct=False,
                            explanation_text="When you submit an offer, you get the best price for all the units that can be matched. In the BUY column are also units with a price of 2, so you must get a price of 2 for some of your units.")
        option2 = Option_MC(question=question, option_text="for a price of 2", idd=2, correct=False,
                            explanation_text="In the BUY column are only 2 units with a price of 2, so you cannot get a price of 2 for all your 3 units.")
        option3 = Option_MC(question=question, option_text="1 unit for a price of 1 and 2 units for a price of 2",
                            idd=3, correct=True,
                            explanation_text="When you submit an offer, you get the best price for all the units that can be matched. In the BUY column there are 2 units with a price of 2 and 1 unit with a price of 1.")
        option4 = Option_MC(question=question, option_text="2 units for a price of 1 and 1 unit for a price of 2",
                            idd=4, correct=False,
                            explanation_text="When you submit an offer, you get the best price for all the units that can be matched. In the BUY column are 2 units with a price of 2, so you must get a price of 2 for at least 2 of your units.")
        to_insert_options.extend([option1, option2, option3, option4])

        ######################################################

        # i=11
        i += 1
        question = cls(treatment=treatment,auction=auction,
                            question_text="Look at the Offer Overview in the picture below. Given the offers at this moment, if I submit a BUY offer of 2 units for a price of 7, how many units do I buy?",
                            id=i, url="staticfiles/images/testing02.png", pic_width=450, pic_height=500, js2=True)
        # question.save()
        to_insert_questions.append(question)
        option1 = Option_MC(question=question, option_text="no units", idd=1, correct=False,
                            explanation_text="The price for which you make your BUY offer is equal or higher than all the three offers in the SELL column of the Offers Overview. Your BUY offer can thus be matched at least to 1 unit.")
        option2 = Option_MC(question=question, option_text="1 unit", idd=2, correct=False,
                            explanation_text="The price for which you make your BUY offer is equal or higher than all the three offers in the BUY column of the Offers Overview. Your BUY offer can thus be matched to at least 2 units.")
        option3 = Option_MC(question=question, option_text="2 units", idd=3, correct=True,
                            url="staticfiles/images/testing02_ answer10.png", pic_width="300", pic_height="400",
                            explanation_text="The price for which you make your BUY offer is equal or higher than all the three offers in the BUY column of the Offers Overview. You thus indeed buy all your 2 units.")
        to_insert_options.extend([option1, option2, option3])

        # i=12
        i += 1
        question = cls(treatment=treatment,auction=auction,
                            question_text="Look at the Offer Overview in the picture below. Given the offers at this moment, we determined before that if I submit a BUY offer of 2 units for a price of 7, I will buy 2 units. For what price(s) will I buy these 2 units?",
                            id=i, url="staticfiles/images/testing02.png", pic_width=450, pic_height=500, js2=True)
        # question.save()
        to_insert_questions.append(question)
        option1 = Option_MC(question=question, option_text="for a price of 7", idd=1, correct=False,
                            explanation_text="When you submit an offer, you get the best price for all the units that can be matched. In the SELL column are also units with a price of 4, so you must get a price of 4 for some of your units.")
        option2 = Option_MC(question=question, option_text="for a price of 4", idd=2, correct=False,
                            explanation_text="In the SELL column is only 1 unit with a price of 4, so you cannot get a price of 4 for both your 2 units.")
        option3 = Option_MC(question=question, option_text="for a price of 5", idd=3, correct=False,
                            explanation_text="When you submit an offer, you get the best price for all the units that can be matched. In the SELL column are also units with a price of 4, so you must get a price of 4 for some of your units.")
        option4 = Option_MC(question=question, option_text="1 units for a price of 4 and 1 unit for a price of 5",
                            idd=4, correct=True,
                            explanation_text="When you submit an offer, you get the best price for all the units that can be matched. In the SELL column is 1 unit with a price of 4, so you must get a price of 4 for 1 unit. The second unit is then bought at the slightly worse (but still acceptable) price of 5.")
        to_insert_options.extend([option1, option2, option3, option4])

        # i=13
        i += 1
        question = cls(treatment=treatment,auction=auction,
                            question_text="Look at the Offer Overview in the picture below. Given the offers at this moment, if I submit a BUY offer of 5 units for a price of 7, what will be the result?",
                            id=i, url="staticfiles/images/testing02.png", pic_width=450, pic_height=500, js2=True)
        # question.save()
        to_insert_questions.append(question)
        option1 = Option_MC(question=question, option_text="I buy the 3 units on offer.", idd=1, correct=False,
                            explanation_text="You submit a BUY offer for 5 units, while there are only 3 units in total in the SELL column. You thus buy 3 units and the two units that are left over are put into the Offer Overview.")
        option2 = Option_MC(question=question,
                            option_text="I buy the 3 units on offer and I post a BUY offer for 2 units for a price of 7.",
                            idd=2, correct=True, url="staticfiles/images/testing02_ answer12.png", pic_width=300,
                            pic_height=400,
                            explanation_text="You submit a BUY offer for 5 units, while there are only 3 units in total in the SELL column. You thus buy 3 units and the two units that are left over a put into the Offer Overview for a price of 7.")
        option3 = Option_MC(question=question, option_text="I post a BUY offer for 5 units for a price of 7.", idd=3,
                            correct=False,
                            explanation_text="You submit a BUY offer for 5 units for a price of 7. They can thus be matched with the 3 units in the SELL column. Only the remaining 2 units are posted as your BUY offer.")
        to_insert_options.extend([option1, option2, option3])

        # i=14
        i += 1
        log.info(i)
        question = cls(treatment=treatment,auction=auction,
                            question_text="Look at the Earnings Overview for the first 10 units in the picture below. At the moment the Retailer hasn't bought any units now. If the Retailer now successfully buys 5 units, what will be the number of the last unit that will be used (and thus marked with a cross)? (Thus, give the highest unit number that will still have a cross).",
                            id=i, url="staticfiles/images/testing13.png", pic_width="300", pic_height="400", js2=True)
        # question.save()
        to_insert_questions.append(question)
        option1 = Option_MC(question=question, option_text="1", idd=1, correct=False,
                            explanation_text="The Retailer bought 5 units, thus the number of units must be higher.")
        option2 = Option_MC(question=question, option_text="2", idd=2, correct=False,
                            explanation_text="The Retailer bought 5 units, thus the number of units must be higher.")
        option3 = Option_MC(question=question, option_text="3", idd=3, correct=False,
                            explanation_text="The Retailer bought 5 units, thus the number of units must be higher.")
        option4 = Option_MC(question=question, option_text="4", idd=4, correct=False,
                            explanation_text="The Retailer bought 5 units, thus the number of units must be higher.")
        option5 = Option_MC(question=question, option_text="5", idd=5, correct=True,
                            url="staticfiles/images/testing14.png", pic_width="200", pic_height="300",
                            explanation_text="The Retailer bought 5 units, thus the number of units is indeed 5.")
        option6 = Option_MC(question=question, option_text="6", idd=6, correct=False,
                            explanation_text="The Retailer bought 5 units, thus the number of units must be lower.")
        to_insert_options.extend([option1, option2, option3, option4, option5, option6])

        # i=15
        i += 1
        log.info(i)
        question = cls(treatment=treatment,auction=auction,
                            question_text="Look at the Production Cost for the first 10 units in the picture below. If the Producer now successfully BUYS 2 units, what will be the number of the last unit that will be used (and marked with a cross)? (Thus, give the highest unit number that will still have a cross).",
                            id=i, url="staticfiles/images/testing14.png", pic_width="300", pic_height="400", js2=True)

        to_insert_questions.append(question)
        option1 = Option_MC(question=question, option_text="1", idd=1, correct=False,
                            explanation_text="The Producer bought only 2 units, thus the number of units must be higher.")
        option2 = Option_MC(question=question, option_text="2", idd=2, correct=False,
                            explanation_text="The Producer bought only 2 units, thus the number of units must be higher.")
        option3 = Option_MC(question=question, option_text="3", idd=3, correct=True,
                            url="staticfiles/images/testing15.png", pic_width="200", pic_height="300",
                            explanation_text="The Producer bought 2 units, thus the number of used units is now indeed 3.")
        option4 = Option_MC(question=question, option_text="4", idd=4, correct=False,
                            explanation_text="The Producer bought 2 units, thus the number of units must be lower.")
        option5 = Option_MC(question=question, option_text="5", idd=5, correct=False,
                            explanation_text="The Producer bought 2 units, thus the number of units must be lower than before.")

        to_insert_options.extend([option1, option2, option3, option4, option5])

        # i=16
        i += 1
        question = cls(treatment=treatment,auction=auction,
                            question_text="Look at the Earnings Overview for the first 10 units in the picture below. If the Retailer now successfully SELLS 5 units, what will then be the number of his/her FIRST unit?",
                            id=i, url="staticfiles/images/testing15.png", pic_width="300", pic_height="400", js2=True)
        # question.save()
        to_insert_questions.append(question)
        option1 = Option_MC(question=question, option_text="-2", idd=1, correct=True,
                            url="staticfiles/images/testing16.png", pic_width="250", pic_height="350",
                            explanation_text="The Retailer sold 5 units, thus the number of used units is now indeed -2. (The Retailer has in effect borrowed 2 units)")
        option2 = Option_MC(question=question, option_text="-1", idd=2, correct=False,
                            explanation_text="The Retailer sold 5 units, thus the number of units must be lower.")
        option3 = Option_MC(question=question, option_text="0", idd=3, correct=False,
                            explanation_text="There are no units with 0 as an index")
        option4 = Option_MC(question=question, option_text="1", idd=4, correct=False,
                            explanation_text="The Retailer sold 5 units, thus the number of units must be lower.")
        option5 = Option_MC(question=question, option_text="2", idd=5, correct=False,
                            explanation_text="The Retailer sold 5 units, thus the number of units must be lower.")

        to_insert_options.extend([option1, option2, option3, option4, option5])

        # i=17
        i += 1
        question = cls(treatment=treatment,auction=auction,
                            question_text="Look at the Earnings Overview for the first 10 units in the picture below. If the Retailer now successfully buys 5 units, what will be the number of the last unit that will be used (and marked with a cross)? (Thus, give the highest unit number that will still have a cross).",
                            id=i, url="staticfiles/images/testing16.png", pic_width="300", pic_height="400", js2=True)

        to_insert_questions.append(question)
        option1 = Option_MC(question=question, option_text="-1", idd=1, correct=False,
                            explanation_text="The Retailer bought 5 units, thus the number of used units must be higher.")
        option2 = Option_MC(question=question, option_text="0", idd=2, correct=False,
                            explanation_text="There are no units with 0 as an index")
        option3 = Option_MC(question=question, option_text="1", idd=3, correct=False,
                            explanation_text="The Retailer bought 5 units, thus the number of used units must be higher.")
        option4 = Option_MC(question=question, option_text="2", idd=4, correct=False,
                            explanation_text="The Retailer bought 5 units, thus the number of used units must be higher.")
        option5 = Option_MC(question=question, option_text="3", idd=5, correct=True,
                            url="staticfiles/images/testing17.png", pic_width="250", pic_height="300",
                            explanation_text="The Retailer bought 5 units, thus the number of used units is now indeed 3. Two out of the 5 units are used to give back the borrowed two units (unit number 0 and number -1). Only the remaining three units contribute to the Earnings ")

        to_insert_options.extend([option1, option2, option3, option4, option5])

        # i=18
        i += 1
        question = cls(treatment=treatment,auction=auction,
                            question_text="If in a round the MARKET UNITS DEMANDED is equal to 42, and there are four Retailers, what will be the UNITS DEMANDED for the Retailers?",
                            id=i)
        # question.save()
        to_insert_questions.append(question)
        option1 = Option_MC(question=question, option_text="each Retailer has 10 as UNITS DEMANDED.", idd=1,
                            correct=False,
                            explanation_text="This is incorrect as then only 40 out of the total of 43 units would be divided over the Retailers.")
        option2 = Option_MC(question=question,
                            option_text="two Retailers each have 10 and the two remaining Retailers each 11 as UNITS DEMANDED.",
                            idd=2, correct=True,
                            explanation_text="This is correct as the MARKET UNITS DEMANDED is divided as equally as possible over the Retailers")
        option3 = Option_MC(question=question,
                            option_text="one Retailer has zero and the three remaining Retailers have 14 as UNITS DEMANDED.",
                            idd=3, correct=False,
                            explanation_text="The MARKET UNITS DEMANDED is divided as equally as possible over the Retailers.")
        option4 = Option_MC(question=question, option_text="The UNITS DEMANDED cannot be determined in this case",
                            idd=4, correct=False,
                            explanation_text="The UNITS DEMANDED can be determined.")
        to_insert_options.extend([option1, option2, option3, option4])

        # i=19
        i += 1
        if treatment.require_units_demanded_on_PR:
            question = cls(treatment=treatment,auction=auction,
                                question_text="If in Stage 2 a Retailer has bought (or a Producer has sold) more units than the number of UNITS DEMANDED. What can the Retailer (or Producer) do to increase profits?",
                                id=i)
            # question.save()
            to_insert_questions.append(question)
            option1 = Option_MC(question=question,
                                option_text="The Retailer (or Producer) can offer to sell (buy back) the excess of units in Stage 2 until the Retailer (or Producer) has exactly the same number as UNITS DEMANDED.",
                                idd=1,
                                correct=True,
                                explanation_text="This is correct. A Retailer will not be credited for holding extra units above the UNITS DEMANDED, and can thus earn some extra profit by selling the extra units. A Producer that has sold more units than the number of UNITS DEMANDED increases his profit by buying back units when the price for these units is below the Producer's production costs.")
            option2 = Option_MC(question=question,
                                option_text="When a Retailers (or Producer) has more units than the number of UNITS DEMANDED in Stage 2, nothing can be done and the Retailer (or Producer) must just accept that they lose a little bit of profit here.",
                                idd=2, correct=False,
                                explanation_text="This is incorrect as both Retailers and Producers are allowed to sell and buy in both Stage 1 and Stage 2. They can thus try to change the number of units sold or bought.")
            option3 = Option_MC(question=question,
                                option_text="A Retailer can always still in Stage 2 try to reduce the number of units it bought by offering to sell units. However, a Producer in Stage 2 cannot try to buy back any excess units.",
                                idd=3, correct=False,
                                explanation_text="This is incorrect as both Retailers and Producers are allowed to sell and buy in both Stage 1 and Stage 2. They can thus try to change the number of units sold or bought.")
            option4 = Option_MC(question=question,
                                option_text="A Producer can always still in Stage 2 try to buy back excess units. However, a Retailer in Stage 2 cannot reduce the number of units it bought by offering to sell units.",
                                idd=4, correct=False,
                                explanation_text="This is incorrect as both Retailers and Producers are allowed to sell and buy in both Stage 1 and Stage 2. They can thus try to change the number of units sold or bought.")
            to_insert_options.extend([option1, option2,option3,option4])
        else:
            question = cls(treatment=treatment, auction=auction,
                           question_text="If in Stage 2 a Retailer has bought more units than the number of UNITS DEMANDED. What can the Retailer do to increase profits?",
                           id=i)
            # question.save()
            to_insert_questions.append(question)
            option1 = Option_MC(question=question,
                                option_text="The Retailer can offer to sell the excess of units in Stage 2 until the Retailer has exactly the same number as UNITS DEMANDED.",
                                idd=1,
                                correct=True,
                                explanation_text="This is correct. A Retailer will not be credited for holding extra units above the UNITS DEMANDED, and can thus earn some extra profit by selling the extra units.")
            option2 = Option_MC(question=question,
                                option_text="When a Retailers has more units than the number of UNITS DEMANDED in Stage 2, nothing can be done and the Retailer must just accept that they lose a little bit of profit here.",
                                idd=2, correct=False,
                                explanation_text="This is incorrect as Retailers (and Producers) are allowed to sell and buy in both Stage 1 and Stage 2. Retailers can thus try to change the number of units sold or bought.")

            to_insert_options.extend([option1, option2])

        msg = cls.objects.bulk_create(to_insert_questions)
        msg = Option_MC.objects.bulk_create(to_insert_options)
        auction = Player_Questions.define_player_questions(auction)
        return i-(UNIQUEIZER * auction.id)

    def __str__(self):  # For Python 2, use __str__ on Python 3
        return "id:{} text:{}".format(self.id, self.question_text)




####################################################################################
# Testing app classes
####################################################################################

class Option_MC(BaseMethods, models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    idd = models.SmallIntegerField(default=0)
    option_text = models.CharField(max_length=400, default="")
    correct = models.BooleanField(default=False)
    explanation_text = models.TextField(max_length=300,default="")
    url = models.SlugField(max_length=200, default="")
    pic_height = models.CharField(max_length=10,default="125")
    pic_width = models.CharField(max_length=10,default="500")


class Player_Questions(BaseMethods, models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    player = models.ForeignKey(Player, default=None,on_delete=models.CASCADE)
    question = models.ForeignKey(Question, default=None,related_name='player_questions', on_delete=models.CASCADE)
    success = models.BooleanField(default=False)
    trials= models.IntegerField(default=0)
    finished = models.BooleanField(default=False)
    pqo_init = models.BooleanField(default=False)

    @classmethod
    def define_player_questions(cls, auction):
        log.info("player_list now ordered by id")
        player_list = Player.objects.filter(auction=auction).order_by('id')
        question_list = Question.objects.all().order_by('id')
        to_insert_pq=[]
        for question in question_list:
            for player in player_list:
                player_question= cls(player=player,question=question)
                # player_question.save()
                to_insert_pq.extend([player_question])
        msg = cls.objects.bulk_create(to_insert_pq)
        log.info("bulk_create pq success!")
        auction.testing_questions_defined=True
        auction.testing_player_questions_defined = True

        auction.save_and_cache()

        return auction


def random_int():
    # random.seed()
    return random.randint(1, 9999)

class Player_Question_Options(BaseMethods, models.Model):

    id = models.BigAutoField(primary_key=True, null=False)
    ord = models.IntegerField(default=random_int,null=True)
    player_question = models.ForeignKey(Player_Questions, default=None, on_delete=models.CASCADE)
    option= models.ForeignKey(Option_MC,on_delete=models.CASCADE)
    reveal = models.BooleanField(default=False)