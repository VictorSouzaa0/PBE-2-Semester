from django.shortcuts import render, redirect
from .models import Everthing
from .forms import EverForm
# Create your views here.

def index(request):
    ever_all = Everthing.objects.all()
    form = EverForm()
    if request.method == 'POST':
        form = EverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, "index.html", {'ever_all' : ever_all, 'form': form})

def update(request, pk):
    alll = Everthing.objects.get(id = pk)
    form = EverForm(instance=all)
    if request.method == 'POST':
        form = Everthing(request.POST, instance=all)
        if form.is_valid():
            form.save
            return redirect('index')
    return render(request, 'update.html',{'form': form, 'alll' : alll})