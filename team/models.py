from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
	YEAR_CHOICES = (
		('YEAR1', '1st year'),
		('YEAR2', '2nd year'),
		('YEAR3', '3rd year'),
		('YEAR4', '4th year')
	)
	COURSE_CHOICES = (
		('BTECH', 'B. Tech.'),
		('MTECH', 'M. Tech.'),
		('MCA', 'MCA')
	)
	name = models.CharField(max_length = 100, null = True)
	regno = models.CharField(max_length = 10, null = False)
	course = models.CharField(max_length = 10, choices = COURSE_CHOICES, blank = True, null = False)
	year = models.CharField(max_length = 10, choices = YEAR_CHOICES, blank = True, null = False)
	registered = models.BooleanField(default = True)

class Team(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length = 50)
	mem1 = models.ForeignKey(Student, related_name = 'leader', null = False)
	mem2 = models.ForeignKey(Student, related_name = 'member2', null = True)
	mem3 = models.ForeignKey(Student, related_name = 'member3', null = True)
	mem4 = models.ForeignKey(Student, related_name = 'member4', null = True)
	points = models.IntegerField(default = 0, null = False)
	lastpoints = models.DateTimeField(null = True)