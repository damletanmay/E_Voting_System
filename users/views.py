from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Voter

def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':

        username = request.POST.get("voter_id")

        # print(username)

        if(username is not None):
            try:
                voter = Voter.objects.get(pk = username)
                print(voter)
                user = auth.authenticate(username = username,password = username)

                if user is not None:
                    auth.login(request,user) #used to login
                    print('User logged in!')
                    return redirect('user_home')
                else:
                    user = User.objects.create_user(username,password = username)
                    auth.login(request,user)
                    print('User Made!')
                    election_data = {'data': getData()}
                    return redirect('user_home')

            except Voter.DoesNotExist:
                return render(request, 'login.html',{'error':"Invalid Voter Id"})




def getData():
    el_date = ['27/02/2021', '28/02/2021']
    el_name = ['17th Loksabha Election', '18th Loksabha Election']
    el_time = ['8:00 - 17:00 (IST)', '8:00 - 17:00 (IST)']

    data = zip(el_date, el_name, el_time)

    return data

@login_required(login_url = '/voting/')
def user_home(request):
    election_data = {'data': getData()}
    return render(request, 'user_home.html', election_data)


@login_required(login_url = '/voting/')
def user_profile(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        voter = Voter.objects.get(pk = username)
        return render(request, 'user_profile.html', {'voter':voter})

@login_required(login_url = '/voting/')
def vote(request):
    prt_name = ['Narendra Modi', 'Rahul Gandhi']
    prt_sym = ['BJP', 'NCI']

    party_data = zip(prt_name, prt_sym)

    election_data = {'name': '17th Loksabha Election', 'party_data': party_data}

    return render(request, 'vote.html', election_data)


@login_required(login_url = '/voting/')
def logout(request):
    auth.logout(request)
    return redirect('home')
