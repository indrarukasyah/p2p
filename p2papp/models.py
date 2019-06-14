from django.db import models

class Slider(models.Model):
    image = models.ImageField()
    layer_one = models.CharField(max_length=200,blank=True,null=True)
    layerone_span = models.CharField(max_length=200,blank=True,null=True)
    layer_two = models.CharField(max_length=200,blank=True,null=True)
    layer_two_span = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return str(self.layer_one)