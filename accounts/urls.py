from django.urls import path

from . import views

urlpatterns = [	path('register', views.register, name="register"),
				path('registerphoto', views.register, name="registerphto"),
				path('registerevent', views.register, name="registerevent"),
			    path('login', views.login, name="login"),
				path('logout', views.logout, name="logout"),
				
				]
