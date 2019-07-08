from django.shortcuts import render,HttpResponse
from .models import *
from blog.models import Post

def homepage(request):
    featured_projects = FeaturedProjects.objects.all()[:5]
    projects = Project.objects.all()
    slides = Slider.objects.all()
    recent_posts = Post.objects.order_by('created_on')[:5]
    sponsors = Sponsor.objects.all()[:10]
    data = {"slides":slides,
            'featured_projects':featured_projects,
            'projects':projects,
            'recent_posts':recent_posts,
            'sponsors':sponsors}
    return render(request,'main/index.html',data)




def project_detail(request,slug):
    project = Project.objects.get(slug=slug)
    data = {'project':project}
    return render(request,'main/project_detail.html',data)