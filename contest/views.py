from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from contest.models import Question, Hint, Solve

def login(request):
	if request.method == "GET":
		if request.user.is_authenticated:
			return redirect('/contest/')
		template = loader.get_template('login.html')
		context = {}
		return HttpResponse(template.render(context, request))
	elif request.method == "POST":
		print(request.POST["csrfmiddlewaretoken"])
		user = authenticate(username = request.POST["uname"], password = request.POST["pw"])
		if user is not None:
			auth_login(request, user)
			return redirect('/contest/')
		else:
			return redirect('/contest/login/')

def logout(request):
	return 0

def main(request):
	if request.user.is_authenticated:
		template = loader.get_template('main.html')
		context = {'questions' : Question.objects.all()}
		return HttpResponse(template.render(context, request))
	else:
		return redirect('/contest/login')

def question(request, question_id = None):
	if question_id is None:
		raise Http404("Invalid question")
	else:
		try:
			q = Question.objects.get(id = question_id)
			hints = q.hints.all()
			template = loader.get_template('question.html')
			context = {'question' : q, 'hints' : hints}
			return HttpResponse(template.render(context, request))
		except Question.DoesNotExist:
			raise Http404("Invalid question")

@csrf_exempt
def submitflag(request):
	if request.method == "POST":
		try:
			q = Question.objects.get(id = request.POST["question"])
			try:
				solved = Solve.objects.get(userteam = request.user, question = q)
				return HttpResponse("solved")
			except Solve.DoesNotExist:
				print("user : " + request.user.username + " question " + str(q.id) + " flag : " + request.POST["flag"])
				if q.answer == request.POST["flag"]:
					Solve(question = q, userteam = request.user).save()
					t = request.user.team
					t.points = t.points + q.points
					t.save()
					return HttpResponse("right")
				else:
					return HttpResponse("wrong")
		except Question.DoesNotExist:
			return HttpResponse("wrong")
	else:
		return HttpResponse("wrong")