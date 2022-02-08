from django import forms
from .models import Strategy


class StrategyForm(forms.ModelForm):
    class Meta:
        model = Strategy
        fields = ('name', 'long_strategy', 'pair',
                  'date_strategy', 'total_amount_of_coin', 'number_of_orders',
                  'margin', 'start_price', 'first_margin', 'max_set_margin', 'use_bnb', 'profit')
        labels = {'name': 'Algorithm', 'long_strategy': 'is long',
                  'pair': 'Pair(ex. \'BNBUSDT\')',
                  'date_strategy': 'Data',
                  'total_amount_of_coin': 'Amounts',
                  'number_of_orders': 'N orders',
                  'margin': 'Margin, %',
                  'start_price': 'Start price',
                  'first_margin': 'First order margin, %', 'max_set_margin': 'Set margin, %',
                  'use_bnb': 'is using bnb for commission',
                  'profit': 'Profit percentage, %'}
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
            'long_strategy': forms.RadioSelect,
            'pair': forms.TextInput(attrs={'placeholder': 'Input the name of pair', 'class': 'form-control'}),
            'date_strategy': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
            'total_amount_of_coin': forms.TextInput(attrs={'placeholder': 'Amount', 'class': 'form-control'}),
            'number_of_orders': forms.TextInput(attrs={'placeholder': 'Number', 'class': 'form-control'}),
            'margin': forms.TextInput(attrs={'placeholder': 'Orders margin', 'class': 'form-control'}),
            'start_price': forms.TextInput(attrs={'placeholder': 'Price', 'class': 'form-control'}),
            'first_margin': forms.TextInput(attrs={'placeholder': 'First order percentage', 'class': 'form-control'}),
            'max_set_margin': forms.TextInput(attrs={'placeholder': 'Percentage', 'class': 'form-control'}),
            'use_bnb': forms.RadioSelect,
            'profit': forms.TextInput(attrs={'placeholder': 'Profit percentage', 'class': 'form-control'}),
        }
