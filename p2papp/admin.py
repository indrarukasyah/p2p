from django.contrib import admin
from .models import Slider
from django.contrib.admin.views.main import ChangeList

class SliderC(admin.ModelAdmin):
    list_filter = ('layer_one',)
    list_display = ('layer_one','layerone_span','layer_two')




admin.site.register(Slider,SliderC)