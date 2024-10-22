from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CAR


def car(request):
    car1 = CAR.objects.all()
    return render(request,'car.html', {'car1': car1})


def index(request):
    
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def chat(request,pk):
    data_set = CAR.objects.get(pk=pk)
    phone_number = int(data_set.phone_number)
    return render(request,'chat.html',{'phone_number':phone_number,'data':data_set})


