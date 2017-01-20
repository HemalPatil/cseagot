from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main, name = 'main'),
	url(r'^register/', views.register, name = 'register'),
	url(r'^checkteam/', views.checkteam, name = 'checkteam'),
	url(r'^successful/', views.successful, name = 'successful')
]