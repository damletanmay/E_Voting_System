from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/voting/')
def home(request):
    return render(request,'templates/election_home.html')
