from django.urls import path
from . import views

urlpatterns = [
     path('', views.candidate_login,name = 'candidate_login'),
     path('voter/', views.candidate_voter,name = 'candidate_voter'),
     path('home/', views.candidate_home,name = 'candidate_home'),
     path('register/<int:election_id>/<str:voter_id>', views.candidate_register,name = 'candidate_register'),
     path('logout/', views.logout,name = 'c_logout'),
 ]
