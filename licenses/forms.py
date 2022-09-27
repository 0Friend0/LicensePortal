from django.forms import ModelForm
from django import forms
from .models import Client, License



class LicenseForm(ModelForm):
    expiration_date = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'), 
                                         attrs={'placeholder': 'dd-mm-yyyy'}))

    class Meta:
        model = License
        fields = '__all__'


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'



