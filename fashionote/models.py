from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

# Create your models here.

class Brand(models.Model):
    """ブランドのモデル"""
    brand_name = models.CharField(max_length=256)
    concept = models.TextField(default='')
    url = models.CharField(max_length=256, blank=True, null=True)
    memo = models.TextField(default='')
    image = models.ImageField(upload_to='img/upload', blank=True, null=True)
    tags = TaggableManager(blank=True)
    create_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
