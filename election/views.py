from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

@login_required
def election_home(request):
    return render(request,'election_home.html');

@login_required
def hold(request):
    return render(request,'hold_election.html');

def password(request):
    if request.method == 'GET':
        return render(request,'election_login.html');
    else:
        superusers = list(User.objects.filter(is_superuser=True))
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == str(superusers[0]):
            user = auth.authenticate(username = username,password = password)
            if user is not None:
                auth.login(request,user)
                return redirect('election_home')
            else:
                return render(request,'election_login.html',{'error':'Your Username or password is incorrect!'})
        else:
            return render(request,'election_login.html',{'error':'Authorized Personnel Only!'})
