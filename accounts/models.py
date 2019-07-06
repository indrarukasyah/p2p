from django.db import models
from django.contrib.auth.models import User
from .choices import gender,COUNTRIES



class Profile(models.Model):
    user       = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name  = models.CharField(max_length=120, null=True, blank=True)
    phone      = models.CharField(max_length=15, blank=True, null=True)
    active     = models.BooleanField(default=False)
    token      = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
