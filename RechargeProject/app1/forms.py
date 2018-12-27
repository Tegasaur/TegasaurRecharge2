from django import forms
from app1.models import CreditCardM
from django.core import validators

class CreditCardF(forms.ModelForm):
    expirydate=forms.DateField(widget=forms.DateInput)
    class Meta():
        model=CreditCardM
        fields= '__all__'
