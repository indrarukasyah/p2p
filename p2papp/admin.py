from django.contrib import admin
from .models import Slider


class SliderC(admin.ModelAdmin):
    list_filter = ('layer_one',)


admin.site.register(Slider,SliderC)