from django.shortcuts import render,redirect,get_object_or_404
from .models import Car
from .form import ItemCar
# Create your views here.

def car_read(request):
    cars = Car.objects.all()
    return render(request, "cars-read.html", {'cars': cars})

def car_create(request):
    if request.method == "POST":
        form = ItemCar(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars')
    else:
        form = ItemCar()

    return render(request, 'car_create.html', {'car': form})

def car_update(request, pk):
    item_car = get_object_or_404(Car,pk=pk)
    if request.method == "PUT":
        form = ItemCar(request.PUT, instance=item_car)
        if form.is_valid():
            form.save()
            return redirect('car_create.html')
    else:
        form = ItemCar(instance=item_car)
        return render(request, 'cars-read.html',{'form': form})
    
def car_delete(request,pk):
    item = get_object_or_404(Car,pk=pk)
    if request.method == "DELETE":
        item.delete()
        return redirect('cars-read')
    return render(request, 'cars_confirm_delete',{'item':item})