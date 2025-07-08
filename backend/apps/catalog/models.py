from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Label(models.Model):
    name      = models.CharField(max_length=50)
    color     = models.CharField(max_length=7, blank=True)  # e.g. "#FF0000"
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name        = models.CharField(max_length=100)
    logo        = models.ImageField(upload_to="brands/logos/", blank=True, null=True)
    description = models.TextField(blank=True)
    is_active   = models.BooleanField(default=True)

    def __str__(self):
        return self.name