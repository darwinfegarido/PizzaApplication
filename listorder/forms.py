from django import forms
from django.db import models
from .models import PizzaType, Pizza, Transaction


class PizzaTypeForm(forms.ModelForm):
    class Meta:
        model = PizzaType
        fields = ['name']

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['pizza_type_id', 'name', 'price']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['pizza_id', 'quantity']

class SearchForm(forms.Form):
    name = forms.CharField(required=False)
