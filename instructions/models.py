# # import random
# from django.db import models
# from dAuction2.models import BaseMethods
# from forward_and_spot.models import Auction
#
# SUMMARY_INSTR = 0
# FULL_INSTR = 1
#
# ITYPES = (
#     (SUMMARY_INSTR, 'SUMMARY INSTRUCTIONS'),
#     (FULL_INSTR, 'FULL INSTRUCTIONS'),
# )
#
# class Page(BaseMethods, models.Model):
#     """ A page in the instructions
#     """
#     auction = models.ForeignKey(Auction, default=None, on_delete=models.CASCADE)
#     id = models.BigAutoField(primary_key=True, null=False)
#     url= models.SlugField(max_length=1,default=None, null=True)
#     idd = models.PositiveSmallIntegerField(default=None, null=True)
#     itype = models.PositiveSmallIntegerField(choices=ITYPES,default=None, null=True)
