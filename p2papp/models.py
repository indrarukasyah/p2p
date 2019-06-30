from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User


class Slider(models.Model):
    image = models.ImageField()
    layer_one = models.CharField(max_length=200,blank=True,null=True,verbose_name='Name')
    layerone_span = models.CharField(max_length=200,blank=True,null=True)
    layer_two = models.CharField(max_length=200,blank=True,null=True)
    layer_two_span = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return str(self.layer_one)



class Investor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dob = models.DateField(blank=True)

    def __str__(self):
        return self.user.username



class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects',blank=True,null=True)
    description = models.TextField()
    fund_needed = models.BigIntegerField()
    is_completed = models.BooleanField(default=False)
    is_activated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def funds_collected(self):
        donation = Fund.objects.filter(project_id=self.id).aggregate(Sum('donation'))
        if donation['donation__sum']:
            return donation['donation__sum']
        else:
            return 0.0


    def donors_count(self):
       return Fund.objects.filter(project_id=self.id).count()


class FeaturedProjects(models.Model):
    project = models.OneToOneField(Project,on_delete=models.CASCADE)

    def __str__(self):
        return self.project.name

class Fund(models.Model):

    invester = models.ForeignKey(Investor,on_delete=models.CASCADE)
    project  = models.ForeignKey(Project,on_delete=models.CASCADE)
    donation = models.BigIntegerField()
    payment_method = models.CharField(max_length=2)


    def __str__(self):
        return self.invester.user.username
