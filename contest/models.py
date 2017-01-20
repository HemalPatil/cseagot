from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	question = models.TextField(null = False)
	answer = models.CharField(max_length = 100, null = False)
	points = models.IntegerField(null = False)

class Hint(models.Model):
	question = models.ForeignKey(User, related_name = 'hints', null = False)
	hint = models.TextField(null = False)

# class File(models.Model):
# 	qfile = models.FileField