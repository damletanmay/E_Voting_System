from django.urls import path
from . import views

# all urls path will go to thier particular view
urlpatterns = [
    path('', views.login,name = 'login'),
    path('user_home/', views.user_home,name = 'user_home'),
    path('user_profile/', views.user_profile,name = 'user_profile'),
    path('otp/', views.otp,name = 'otp'),
    path('vote/<int:election_id>/', views.vote,name = 'vote'),# <int: election_id> is there, so that dynamic path can be created
    path('logout/', views.logout,name = 'logout'),
]
