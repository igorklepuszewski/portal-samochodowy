from .models import Car, CarDetail, CarMain
from django.forms import ModelForm, DateInput
from django import forms

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['main', 'detail']


class CarDetailForm(ModelForm):
    production_date_start = forms.DateField(widget=DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date',}
            ))
    production_date_end = forms.DateField(widget=DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date',}
            ))
    power_min = forms.IntegerField(min_value=0)
    power_max = forms.IntegerField(min_value=0)
    class Meta:
        model = CarDetail
        exclude = ('car', 'power', 'production_date')


class CarMainForm(ModelForm):
    class Meta:
        model = CarMain
        exclude = ('car', )
