from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from contest.models import Question, Hint

def login(request):
	if request.method == "GET":
		template = loader.get_template('login.html')
		context = {}
		return HttpResponse(template.render(context, request))
	#elif request.method == "POST":