from django.urls import path
from django.contrib.auth import views as auth_view



urlpatterns=[
path('login/', auth_view.LoginView.as_view(
	
	template_name='usuarios/form_login.html'), name='login'),
]