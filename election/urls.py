from django.urls import path
from . import views

urlpatterns = [
    path('',views.election_home,name='election_home'),
    path('password',views.password,name='password'),
    path('hold',views.hold,name='hold'),
]
