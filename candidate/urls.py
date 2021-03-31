from django.urls import path
from . import views

urlpatterns = [
     path('', views.candidate_login,name = 'candidate_login'),
     path('register/', views.candidate_register,name = 'candidate_register'),
     path('logout/', views.logout,name = 'c_logout'),
 ]
