from django.shortcuts import render
from .models import Sketch,Samima,Mithila,Isrita,Bintu,Puspo,Tonima
#,Tonima,Mithila,Isrita,Bintu,Puspo

def home(request):
    s=Sketch.objects.all()

    return render(request,"home.html",{'s':s}) 

# Create your views here.
def samima(request):
    s=Samima.objects.all()

    return render(request,"artist.html",{'s':s}) 

def tonima(request):
    s=Tonima.objects.all()

    return render(request,"artist.html",{'s':s}) 

def mithila(request):
    s=Mithila.objects.all()

    return render(request,"artist.html",{'s':s}) 

def isrita(request):
    s=Isrita.objects.all()

    return render(request,"artist.html",{'s':s}) 

def bintu(request):
    s=Bintu.objects.all()

    return render(request,"artist.html",{'s':s}) 

def puspo(request):
    s=Puspo.objects.all()

    return render(request,"artist.html",{'s':s}) 