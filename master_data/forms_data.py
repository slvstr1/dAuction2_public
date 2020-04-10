__author__ = 'MSIS'

from django import forms
from forward_and_spot.models import Auction
from django.forms import NumberInput, Select, Textarea, CheckboxInput, IntegerField

RANDOMIZE=[('True','True'),
              ('False','False')]
# DISTRIBUTION=[('uniform',1),('normal',0)]



class DataForm(forms.ModelForm):
    # An inline class to provide additional information on the form.
    particular_info = forms.Textarea()
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Auction
        fields = ('is_part_experiment', 'particular_info')
        widgets = {
            'is_part_experiment': CheckboxInput(attrs={'style': 'width:75px; height:22px'}),
            'particular_info':
                Textarea(attrs={'style': 'width:1375px; height:60px', 'required': False}),
                 }
