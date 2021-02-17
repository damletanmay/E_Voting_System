from django.shortcuts import render

def login(request):
    return render(request, 'login.html')


def user_home(request):
    return render(request, 'user_home.html')


def user_profile(request):
    return render(request, 'user_profile.html')


def vote(request):
    return render(request, 'vote.html')

