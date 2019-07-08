from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Author(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)
    bio = models.TextField(blank=True,null=True)
    profile_image = models.ImageField(blank=True,null=True,upload_to='author_images')


    def __str__(self):
        return self.first_name+" "+self.last_name


STATUS = (('D','Draft'),('P','Publish'))

class Tag(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(blank=True,null=True)
    slug = models.SlugField(blank=True, null=True,unique=True)
    featured_image = models.ImageField(blank=True, null=True, upload_to='featured_images')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS, default='D')
    created_on = models.DateField(auto_now_add=True)
    shares = models.BigIntegerField(default=20)
    views = models.BigIntegerField(default=1000)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return str(self.slug)

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)


