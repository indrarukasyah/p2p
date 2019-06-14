from django.shortcuts import render,HttpResponse
from .models import *

def homepage(request):
    slides = Slider.objects.all()
    data = {"slides":slides}
    return render(request,'main/index.html',data)

