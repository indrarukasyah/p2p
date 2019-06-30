from django.contrib import admin
from .models import *
from django import forms
from django.contrib.admin.views.main import ChangeList

class ProjectForm(forms.ModelForm):  #OVERRIDING Scenario Admin Form Fields
    class Meta:
        model = Project
        exclude = ['funds_collected']



class ProjectCustomAdmin(admin.ModelAdmin):
    #Overiding Project Changeform form
    form =  ProjectForm

class SliderCustomAdmin(admin.ModelAdmin):
    list_filter = ('layer_one',)
    list_display = ('layer_one','layerone_span','layer_two','layer_two_span')


admin.site.register(Slider,SliderCustomAdmin)
admin.site.register(Project,ProjectCustomAdmin)
admin.site.register(Investor)
admin.site.register(Fund)
admin.site.register(FeaturedProjects)