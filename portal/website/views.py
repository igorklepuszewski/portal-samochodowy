from django.shortcuts import render

# Create your views here.
from car.forms import CarForm, CarDetailForm, CarMainForm


def main_view(request):
    context = {}
    template = "main.html"
    if request.method == 'GET':
        car_detail_form = CarDetailForm(prefix='detail')
        car_main_form = CarMainForm(prefix='main')
        context["car_detail_form"] = car_detail_form
        context["car_main_form"] = car_main_form
        return render(request, template, context)