from django.shortcuts import render,redirect,HttpResponse
from users.models import Voter
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def candidate_login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('candidate_register')
        else:
            return render(request, 'candidate_login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        voter_id = request.POST.get('voter_id')

        if username is not None:
            try:
                voter = Voter.objects.get(pk = voter_id)
                superusers = list(User.objects.filter(is_superuser=True))
                username = request.POST.get("username")
                password = request.POST.get("password")

                if username == str(superusers[0]):
                    user = auth.authenticate(username = username,password = password)
                    if user is not None:
                        auth.login(request,user)
                        return redirect('candidate_register')
                    else:
                        return render(request,'candidate_login.html',{'error':'Your Username or password is incorrect!'})
                else:
                    return render(request,'candidate_login.html',{'error':'Authorized Personnel Only!'})

            except Voter.DoesNotExist:
                return render(request, 'candidate_login.html',{'error':"Invalid Voter Id"})


@login_required(login_url = '/candidate/')
def candidate_register(request):
    if request.user.is_superuser:
        return render(request,'register.html');
    else:
        return HttpResponse("Authorized Personnel Only !")


@login_required(login_url = '/candidate/')
def logout(request):
    auth.logout(request)
    return redirect('candidate_login')
