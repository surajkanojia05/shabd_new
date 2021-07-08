from django.shortcuts import render
from home.models import famous_ghazal, ghazal_home, new_ghazal


# Create your views here.
def index(request):
    shayari=ghazal_home.objects.all()
    return render(request,'index.html',{'shayari':shayari})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request, "contact.html")

def new_ghazals(request):
    shayari=new_ghazal.objects.all()
    return render(request, "new_ghazals.html", {'shayari':shayari})

def famous_ghazals(request):
    shayari=famous_ghazal.objects.all()
    return render(request, "famous_ghazals.html", {'shayari':shayari})