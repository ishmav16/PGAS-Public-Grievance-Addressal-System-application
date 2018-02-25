from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Stock1(models.Model):
    data=models.TextField(
        db_column='data',
        blank=True)
    desc= models.TextField(blank=True)
    lati=models.TextField(blank=True)
    long=models.TextField(blank=True)
    email1=models.TextField(blank=True)
    status = models.IntegerField(default = 0,blank=True)
    priority=models.IntegerField(default=0,blank=True)
    def __str__(self):
        return self.desc

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    #phone_= models.CharField(max_length=10, null=False, blank=False)
    adhar_no=models.IntegerField( null=False, blank=False)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Useer(models.Model):
	user1=models.CharField(max_length=15)
	pass1=models.CharField(max_length=15)
	email1=models.CharField(max_length=20)
	Adhar=models.CharField(max_length=14,default = '1234-5678-9012')

class Dummy(models.Model):
	duser1=models.CharField(max_length=15)
	bf=models.IntegerField(default=0)
	def __str__(self):
		return self.duser1
