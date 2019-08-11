from django.db import models

# Create your models here.


class AadharData(models.Model):

	id = models.IntegerField(primary_key=True),
	aid = models.CharField(unique=True, null=False, blank=False, max_length=128),
	cid = models.IntegerField(null=True, blank=True),
	fingerPrint = models.CharField(unique=True, null=False, blank=False, max_length=256),
	mobile_num = models.CharField(unique=True, null=False, blank=False, max_length=15)
