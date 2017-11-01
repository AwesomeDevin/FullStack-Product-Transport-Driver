# -*- coding:utf-8 -*-
from django.db import models


# Create your models here.


class User(models.Model):
    create_time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=128, blank=True)
    tel = models.CharField(max_length=128, blank=True)
    pwd = models.CharField(max_length=128, blank=True)
    user_img = models.CharField(max_length=128, blank=True)
    car_plate = models.CharField(max_length=128, blank=True)
    money = models.CharField(max_length=128, blank=True)


class Headimage(models.Model):
    user = models.ForeignKey(User)
    img  = models.FileField(upload_to='upload/',blank=True)



class Order(models.Model):
    create_time = models.DateTimeField(auto_now=True)
    appoint_time = models.DateTimeField(auto_now=True)
    startSite = models.CharField(max_length=128, blank=True)
    endSite = models.CharField(max_length=128, blank=True)
    payer = models.CharField(max_length=128, blank=True)
    payer_tel = models.CharField(max_length=128, blank=True)
    picker = models.CharField(max_length=128, blank=True)
    picker_tel = models.CharField(max_length=128, blank=True)
    distance = models.CharField(max_length=128, blank=True)
    duration = models.CharField(max_length=128, blank=True)
