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


    def __init__(self, *args, **kwargs):
        super(CarDetailForm, self).__init__(*args, **kwargs)
        self.fields['color'].required = False
        self.fields['seats'].required = False
        self.fields['fuel'].required = False
        self.fields['production_date_end'].required = False
        self.fields['production_date_start'].required = False
        self.fields['power_min'].required = False
        self.fields['power_max'].required = False


class CarMainForm(ModelForm):
    class Meta:
        model = CarMain
        exclude = ('car', )

    def __init__(self, *args, **kwargs):
        super(CarMainForm, self).__init__(*args, **kwargs)
        self.fields['model'].required = False
        self.fields['make'].required = False
