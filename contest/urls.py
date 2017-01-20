from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main, name = 'main'),
	url(r'^login/', views.login, name = 'login'),
	url(r'^logout/', views.logout, name = 'logout'),
	url(r'^question/(?P<question_id>[0-9]+)/', views.question, name = 'question'),
	url(r'^submitflag/', views.submitflag, name = 'submitflag')
]