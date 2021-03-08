from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.login,name = 'login'),
    path('user_home', views.user_home,name = 'user_home'),
    path('user_profile', views.user_profile,name = 'user_profile'),
    path('vote', views.vote,name = 'vote'),
    path('logout', views.logout,name = 'logout'),
]
