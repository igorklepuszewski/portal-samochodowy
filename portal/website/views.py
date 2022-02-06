from django.shortcuts import render

# Create your views here.
from car.forms import CarForm, CarDetailForm, CarMainForm
from car.models import Car, CarDetail, CarMain


def main_view(request):
    context = {}
    template = "main.html"
    if request.method == 'GET':
        car_detail_form = CarDetailForm(prefix='detail')
        car_main_form = CarMainForm(prefix='main')
        context["car_detail_form"] = car_detail_form
        context["car_main_form"] = car_main_form
        return render(request, template, context)
    if request.method == "POST":
        car_detail_form = CarDetailForm(request.POST, prefix='detail')
        car_main_form = CarMainForm(request.POST, prefix='main')
        if car_detail_form.is_valid() and car_main_form.is_valid():
            make = car_main_form.cleaned_data['make']
            model = car_main_form.cleaned_data['model']
            color = car_detail_form.cleaned_data['color']
            seats = car_detail_form.cleaned_data['seats']
            fuel = car_detail_form.cleaned_data['fuel']
            power_min = car_detail_form.cleaned_data['power_min']
            power_max = car_detail_form.cleaned_data['power_max']
            production_date_start = car_detail_form.cleaned_data['production_date_start']
            production_date_end = car_detail_form.cleaned_data['production_date_end']
            cars = Car.objects.select_related("main").select_related("detail").filter(
                main__make=make,
                main__model=model,
                detail__color=color,
                detail__seats=seats,
                detail__fuel=fuel,
                detail__power__gte=power_min,
                detail__power__lte=power_max,
                detail__production_date__gte=production_date_end,
                detail__production_date__lte=production_date_start,
            )
            context['cars'] = cars
        context["car_detail_form"] = car_detail_form
        context["car_main_form"] = car_main_form
        return render(request, template, context)

