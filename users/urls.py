from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name = 'login'),
    path('user_home/', views.user_home,name = 'user_home'),
    path('user_profile/', views.user_profile,name = 'user_profile'),
    path('vote/<int:election_id>/', views.vote,name = 'vote'),
    path('logout/', views.logout,name = 'logout'),
]
