__author__ = 'MSIS'

from django import forms
from forward_and_spot.models import Player
from django.forms import NumberInput, Select,TextInput,Textarea

YESNO = [(True,'YES'),
              (False,'NO')]
SEX=[(True,'male'),
              (False,'female')]
DIFFICULT=[('1','very easy'),
            ('2','somewhat easy'),
            ('3','not easy, not difficult'),
            ('4','a bit difficult'),
            ('5','very difficult'),
           ]

INTERESTING=[('1','very uninteresting'),
            ('2','somewhat uninteresting'),
            ('3','not uninteresting, not interesting'),
            ('4','a bit interesting'),
            ('5','very interesting'),
           ]

class QuestionnaireForm(forms.ModelForm):
    # An inline class to provide additional information on the form.
    class Meta:
            # Provide an association between the ModelForm and a model
            model = Player
            fields = ('male','age','done_before','difficult_rating', 'interesting_rating','income_monthly_CZK','time_spend_reading','comments','do_better_what')
            labels = {
                'done_before':('Have you done (a version) of this experiment before?'),

            'difficult_rating': ('How difficult was the experiment?'),
            'interesting_rating': ('How interesting was the experiment?'),
            'income_monthly_CZK': ('What is approximately your monthly income in Czech Crowns?'),
            'time_spend_reading': ('How much time (in minutes) did you spend approximately reading the instructions before coming to the experiment?'),
            'comments': ('Do you have any comments?'),
            'do_better_what': ('What could we organize or program better for a next time?'),
        }
            widgets = {


                'done_before':Select(choices=YESNO, attrs={'style':'width:150px; height:35px'}),
                'male': Select(choices=SEX, attrs={'style':'width:150px; height:35px'}),
                'age': NumberInput(attrs={'style':'width:275px; height:35px'}),
                'difficult_rating': Select(choices=DIFFICULT, attrs={'style':'width:150px; height:35px'}),
                'interesting_rating': Select(choices=INTERESTING, attrs={'style':'width:150px; height:35px'}),
                'income_monthly_CZK': NumberInput(attrs={'style':'width:275px; height:35px'}),
                'time_spend_reading': NumberInput(attrs={'style': 'width:275px; height:35px'}),
                'comments': Textarea(attrs={'style':'width:675px; height:135px'}),
                'do_better_what': Textarea(attrs={'style':'width:675px; height:235px'}),
            }

class QuestionnaireIdForm(forms.ModelForm):
    # An inline class to provide additional information on the form.
    class Meta:
            # Provide an association between the ModelForm and a model
            model = Player
            fields = ('first_name','last_name','id_or_birth_number')
            labels = {
                'id_or_birth_number': ('The id number of an official identification document (passport, national id card) or your  birth number (rodne cislo)'),
        }
            widgets = {
                'first_name': TextInput(attrs={'style':'width:275px; height:35px', 'autocomplete':'off'}),
                'last_name': TextInput(attrs={'style':'width:275px; height:35px', 'autocomplete':'off'}),
                'id_or_birth_number': TextInput(attrs={'style': 'width:275px; height:35px', 'autocomplete': 'off'}),
            }