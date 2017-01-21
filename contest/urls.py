from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main, name = 'main'),
	url(r'^login/', views.teamlogin, name = 'teamlogin'),
	url(r'^logout/', views.teamlogout, name = 'teamlogout'),
	url(r'^question/(?P<question_id>[0-9]+)/', views.question, name = 'question'),
	url(r'^submitflag/', views.submitflag, name = 'submitflag'),
	url(r'^leaderboard/', views.leaderboard, name = 'leaderboard')
]