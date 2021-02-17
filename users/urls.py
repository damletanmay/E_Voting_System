from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.login),
    path('user_home', views.user_home),
    path('user_profile', views.user_profile),
]
