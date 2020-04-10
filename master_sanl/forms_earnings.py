__author__ = 'MSIS'

from django import forms
from forward_and_spot.models import Auction
from django.forms import NumberInput, Select, Textarea, CheckboxInput, IntegerField



class AuctionCorrectionForm(forms.ModelForm):
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Auction
        fields = (
        'multiplier', 'multiplier_PR', 'multiplier_RE','fixed_uplift', 'fixed_uplift_PR', 'fixed_uplift_RE')
        widgets = {
            'multiplier': NumberInput(attrs={'style': 'width:50px; height:22px'}),
            'multiplier_PR': NumberInput(attrs={'style': 'width:50px; height:22px'}),
            'multiplier_RE': NumberInput(attrs={'style': 'width:50px; height:22px'}),

            'fixed_uplift': NumberInput(attrs={'style': 'width:50px; height:22px'}),
            'fixed_uplift_PR': NumberInput(attrs={'style': 'width:50px; height:22px'}),
            'fixed_uplift_RE': NumberInput(attrs={'style': 'width:50px; height:22px'}),
        }
