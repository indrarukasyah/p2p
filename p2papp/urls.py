from django.urls import path,include
from .views import *

urlpatterns = [
    path('',homepage,name='homepage'),
    path('project/<slug>',project_detail,name='project'),
]
