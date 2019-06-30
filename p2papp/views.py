from django.shortcuts import render,HttpResponse
from .models import *

def homepage(request):
    featured_projects = FeaturedProjects.objects.all()[:5]
    projects = Project.objects.all()
    slides = Slider.objects.all()
    data = {"slides":slides,'featured_projects':featured_projects,'projects':projects}
    return render(request,'main/index.html',data)

