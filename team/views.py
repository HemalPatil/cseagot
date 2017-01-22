from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.models import User
from team.models import Student, Team
import string
import random

def register(request):
	template = loader.get_template('register.html')
	context = {}
	return HttpResponse(template.render(context, request))

def successful(request):
	template = loader.get_template('successful.html')
	context = {}
	return HttpResponse(template.render(context, request))

@csrf_exempt
def checkteam(request):
	if request.method == "POST":
		print(request.POST['teamname'])
		try:
			team = Team.objects.get(name = request.POST['teamname'])
			return HttpResponse("Team already registered")
		except Team.DoesNotExist:
			print("team does not exist")
			if request.POST["pw"] == "":
				return HttpResponse("Enter password")
			print("mem1" + request.POST['mem1'] + "mem1")
			print("mem2" + request.POST['mem2'] + "mem2")
			print("mem3" + request.POST['mem3'] + "mem3")
			print("mem4" + request.POST['mem4'] + "mem4")
			m1 = None
			m2 = None
			m3 = None
			m4 = None
			try:
				m1 = Student.objects.get(regno = request.POST['mem1'])
				if m1.registered:
					return HttpResponse("Member 1 already registered")
				if request.POST['mem2'] != "":
					try:
						m2 = Student.objects.get(regno = request.POST['mem2'])
						if m2.registered:
							return HttpResponse("Member 2 already registered")
						if request.POST['mem3'] != "":
							try:
								m3 = Student.objects.get(regno = request.POST['mem3'])
								if m3.registered:
									return HttpResponse("Member 3 already registered")
								if request.POST['mem4'] != "":
									try:
										m4 = Student.objects.get(regno = request.POST['mem4'])
										if m4.registered:
											return HttpResponse("Member 4 already registered")
									except Student.DoesNotExist:
										return HttpResponse("Member 4 not registered for competition")
							except Student.DoesNotExist:
								return HttpResponse("Member 3 not registered for competition")
					except Student.DoesNotExist:
						return HttpResponse("Member 2 not registered for competition")
			except Student.DoesNotExist:
				print("illegal mem1 regno")
				return HttpResponse("Member 1 not registered for competition")
			if m1 != None:
				m1.registered = True
				m1.save()
			if m2 != None:
				m2.registered = True
				m2.save()
			if m3 != None:
				m3.registered = True
				m3.save()
			if m4 != None:
				m4.registered = True
				m4.save()
			print("team pw : " + pw)
			uname = request.POST['teamname'].replace(" ", "")
			u = User.objects.create_user(username = uname, password = request.POST["pw"])
			Team(user = u, name = request.POST['teamname'], mem1 = m1, mem2 = m2, mem3 = m3, mem4 = m4).save()
			return HttpResponse("teamreged")
	else:
		raise Http404("Not allowed")