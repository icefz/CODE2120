from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
	path(r'hello/',  views.hello),
	#path(r'example_post/', views.example_post),
	#path(r'example_post/', views.example_post),
	#path(r'example_post/', views.example_post),
	#path(r'example_post/', views.example_post),
	
]