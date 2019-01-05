from django.urls import path
from . import views


urlpatterns = [
	path('', views.post_list, name = 'post_list'),
	#int:pk se refiere a que a la vista le va a pasar un entero en una variable pk
	path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
	path('post/new/', views.post_new, name = 'post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name = 'post_edit'),
	path('drafts/', views.post_draft_list, name = 'post_draft_list'),
	path('post/<int:pk>/publish/', views.post_publish, name = 'post_publish'),
	path('post/<int:pk>/remove/', views.post_remove, name = 'post_remove'),
]