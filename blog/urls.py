from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name = 'post_list'),
	#int:pk se refiere a que a la vista le va a pasar un entero en una variable pk
	path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
]