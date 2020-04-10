__author__ = 'MSIS'

from django import forms
from forward_and_spot.models import Auction, Treatment, Player

# from django.forms import NumberInput,Select, TextInput
from django.forms import NumberInput, Select, Textarea, CheckboxInput, IntegerField
# from django.db.models import Q

RANDOMIZE=[('True','True'),
              ('False','False')]


class TreatmentFormInstanceOnly(forms.ModelForm):
    idd = forms.ModelChoiceField(queryset=Treatment.objects.all().values_list('idd',flat=True).order_by('idd'), to_field_name="idd")

    def __init__(self, *args, **kwargs):
        # print('justhere1')
        auctionid = kwargs.pop('auctionid', None)
        # print('justhere2')
        super(TreatmentFormInstanceOnly, self).__init__(*args, **kwargs)
        # print('justhere3')
        # print("auctionid:{}".format(auctionid))
        if auctionid:
            # print('justhere4')
            self.fields['idd'].queryset = Treatment.objects.filter(au=auctionid).values_list('idd',flat=True).order_by('idd')

    class Meta:
        model = Treatment
        fields = ('idd',)


class TreatmentFormTheoreticalValues(forms.ModelForm):
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Treatment
        fields = ('demand_avg_theory', 'price_avg_theory', 'demand_sd_theory', 'price_sd_theory',)
        widgets = {
            'demand_avg_theory': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'price_avg_theory': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'demand_sd_theory': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'price_sd_theory': NumberInput(attrs={'style': 'width:75px; height:22px'}),
        }


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


class AuctionFormTimeRefreshOnly(forms.ModelForm):
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Auction
        fields = ('time_refresh_data',)
        widgets = {
            'time_refresh_data': NumberInput(attrs={'style': 'width:75px; height:22px'}),
                 }

class AuctionFormRealizedAndSampleValues(forms.ModelForm):
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Auction
        fields = ( 'cov_DP','testing_totalquestions', 'demand_avg', 'price_avg', 'demand_sd','price_sd')
        widgets = {
            'demand_avg': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'price_avg': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'demand_sd': NumberInput(attrs={'style': 'width:75px; height:22px'}),

            'price_sd': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'cov_DP': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            # 'instruction_totalPages': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'testing_totalquestions': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'time_refresh_data': NumberInput(attrs={'style': 'width:75px; height:22px'}),
        }


class TreatmentFormParameterValues(forms.ModelForm):
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Treatment
        fields = ('total_groups', "PR_per_group", "RE_per_group","shedding", 'groups_assignment_alternate', 'd_draws_needed','a','distribution_used',
                  # 'uniform_min','uniform_max',
                  # 'mu', 'sigma',
                  'retail_price', 'ECU_per_CZK_PR', 'ECU_per_CZK_RE', 'start_capital_in_CZK')
        widgets = {
            'groups_assignment_alternate': Select(choices=RANDOMIZE,attrs={'style':'width:75px; height:22px'}),
            'total_groups': NumberInput(attrs={'style':'width:75px; height:22px'}),
            "PR_per_group": NumberInput(attrs={'style': 'width:75px; height:22px'}),
            "RE_per_group": NumberInput(attrs={'style': 'width:75px; height:22px'}),
            "shedding": NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'd_draws_needed': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'a': NumberInput(attrs={'style':'width:75px; height:22px'}),
            'distribution_used': Select(choices=Treatment.DISTRIBUTION_CHOICES, attrs={'style': 'width:75px; height:22px'}),
            # 'uniform_min': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            # 'uniform_max': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            # 'mu': NumberInput(attrs={'style':'width:75px; height:22px'}),
            # 'sigma': NumberInput(attrs={'style':'width:75px; height:22px'}),
            'retail_price': NumberInput(attrs={'style':'width:75px; height:22px'}),
            'ECU_per_CZK_PR': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'ECU_per_CZK_RE': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'start_capital_in_CZK':NumberInput(attrs={'style': 'width:75px; height:22px'}),
                 }

class TreatmentFormParameterValues_uniform(TreatmentFormParameterValues):
    class Meta(TreatmentFormParameterValues.Meta):
        fields =TreatmentFormParameterValues.Meta.fields + ( 'uniform_max', 'uniform_min')
        widgets = TreatmentFormParameterValues.Meta.widgets.update( {
            'uniform_min': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'uniform_max': NumberInput(attrs={'style': 'width:75px; height:22px'}),
        })

class TreatmentFormParameterValues_normal(TreatmentFormParameterValues):
    class Meta(TreatmentFormParameterValues.Meta):
        fields =TreatmentFormParameterValues.Meta.fields + ('mu', 'sigma',)
        widgets = TreatmentFormParameterValues.Meta.widgets.update( {
            'mu': NumberInput(attrs={'style':'width:75px; height:22px'}),
            'sigma': NumberInput(attrs={'style':'width:75px; height:22px'}),
        })



class TimerForm(forms.ModelForm):
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Treatment
        fields = ( 'time_for_instructions','time_for_distribution','time_conditional','time_for_forward_1', 'time_for_forward_2', 'time_for_forward_waiting', 'time_for_spot_1','time_for_spot_2','time_for_spot_3',
                  'time_for_spot_waiting', 'time_for_question_page', 'time_for_testing','total_periods','qp_every', 'time_refresh_check',
                  # 'time_timer_check',
                  )
        widgets = {

            'time_for_instructions': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'time_for_distribution': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'time_conditional': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'time_for_forward_1': NumberInput(attrs={'style':'width:75px; height:22px'}),
            'time_for_forward_2': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'time_for_forward_waiting': NumberInput(attrs={'style':'width:75px; height:22px'}),
            'time_for_spot_1': NumberInput(attrs={'style':'width:75px; height:22px'}),
            'time_for_spot_2': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'time_for_spot_3': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'time_for_spot_waiting': NumberInput(attrs={'style':'width:75px; height:22px'}),
            'time_for_question_page': NumberInput(attrs={'style':'width:75px; height:22px'}),
            'time_for_testing': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'total_periods': NumberInput(attrs={'style':'width:75px; height:22px'}),
            'qp_every': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            'time_refresh_check': NumberInput(attrs={'style': 'width:75px; height:22px'}),
            # 'time_timer_check': NumberInput(attrs={'style': 'width:75px; height:22px'}),
                 }
ROLES =[('RE','RE'),
           ('PR','PR')]

class PlayerForm(forms.ModelForm):
    # An inline class to provide additional information on the form.
    # auction=Auction.objects.get(active=True)
    # player= forms.ModelChoiceField(queryset=Player.objects.filter(auction=auction).order_by('user_id'))
    player = forms.ModelChoiceField(queryset=Player.objects.all().order_by('-selected',"group_id",'user_id'))
    # what to do here? players should be selected by auction, eg:
    # player= forms.ModelChoiceField(queryset=Player.objects.filter(auction=auction).order_by('user_id'))
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Player
        fields = ('id','player', 'role','group')
        widgets = {
            'role': Select(choices=ROLES,attrs={'style':'width:75px; height:22px'}),}