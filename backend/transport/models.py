from django.db import models
import os


# Create your models here.
from serializers import *
# 任务执行基本信息
class User(models.Model):
    create_time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=128, blank=True)
    tel = models.CharField(max_length=128, blank=True)
    pwd = models.CharField(max_length=128, blank=True)
    user_img = models.CharField(max_length=128, blank=True)



    #def __unicode__(self):
    #    return self.title

    # class Meta:
    #     ordering = ('-create_time',)