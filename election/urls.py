from django.urls import path
from . import views

# url requests will be made here which will redirect them to their particular view
urlpatterns = [
    path('',views.election_home,name='election_home'),
    path('password',views.password,name='password'),
    path('hold',views.hold,name='hold'),
]
