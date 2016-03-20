from django.db import models
import datetime
from time import time
from django.utils import timezone

# Create your models here.

#File Upload Function
def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

class Article(models.Model):
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50,default='')
	category = models.CharField(max_length=50,default='')
	body = models.TextField()
	hero_image = models.FileField(upload_to=get_upload_file_name,default='')
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField(default=0)

	def __str__(self):
		return self.title

class Comment(models.Model):
	name = models.CharField(max_length=50,default='')
	body = models.TextField(default='')
	pub_date = models.DateTimeField('date published')
	article = models.ForeignKey(Article)

