from django.shortcuts import render, redirect
from .froms import DataForm
from .models import Data

# Create your views here.

def index(request):

    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main-predictions')
    else:
        form = DataForm()

    context ={
        'form':form
    }
    return render(request,'main/index.html',context)

def predictions(request):
    data = Data.objects.all()
    context ={
        'data':data
    }
    return render(request,'main/predictions.html',context)