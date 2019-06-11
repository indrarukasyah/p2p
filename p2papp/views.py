from django.shortcuts import render,HttpResponse

def homepage(request):
    """Simple homepage View """
    return HttpResponse('Homepage')

