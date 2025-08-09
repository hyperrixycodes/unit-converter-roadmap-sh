from django.shortcuts import render, redirect, get_object_or_404
from .forms import LengthForm, WeightForm, TemperatureForm
from . converters import convert_length, convert_temperature, convert_weight
# Create your views here.

def home(request):
    return render(request, 'converter/base.html')

def length(request):
    result = None
    if request.method == "POST":
        form = LengthForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']
            result = convert_length(value=value, from_unit=from_unit, to_unit=to_unit)
    else:
        form = LengthForm()
    
    return render(request, 'converter/length.html', {
        'form': form,
        'result': result
    })

def weight(request):
    result = None
    if request.method == "POST":
        form = WeightForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']
            result = convert_weight(value, from_unit, to_unit)
    else:
        form = WeightForm()

    return render(request, 'converter/weight.html', {
        'form': form,
        'result': result
    })

def temperature(request):
    result = None
    value, from_unit, to_unit = None, None, None
    if request.method == "POST":
        form = TemperatureForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']
            result = convert_temperature(value, from_unit, to_unit)
    else:
        form = TemperatureForm()
    return render(request, 'converter/temperature.html', {
        'form': form,
        'result': result,
        'from_unit': from_unit,
        'to_unit': to_unit,
        'value': value,
    })