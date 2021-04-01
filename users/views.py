from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Voter
from election.models import Election


def login(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('user_home')
        else:
            return render(request, 'login.html')

    elif request.method == 'POST':
        superusers = list(User.objects.filter(is_superuser=True))
        username = request.POST.get("voter_id")

        if username == str(superusers[0]):
            return redirect('password')
        else:
            if(username is not None):
                try:
                    voter = Voter.objects.get(pk = username)
                    user = auth.authenticate(username = username,password = username)

                    if user is not None:
                        auth.login(request,user) # used to login
                        return redirect('user_home')
                    else:
                        user = User.objects.create_user(username,password = username)
                        auth.login(request,user) # to make user
                        election_data = {'data': getData()}
                        return redirect('user_home')

                except Voter.DoesNotExist:
                    return render(request, 'login.html',{'error':"Invalid Voter Id"})


def getData():
    election = Election. objects.all()
    return election

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
def vote(request,election_id):
    if request.method == 'GET':

        election =  Election.objects.get(pk = election_id)
        if isEligible(request,election):

            prt_name = ['Narendra Modi', 'Rahul Gandhi']
            prt_sym = ['BJP', 'NCI']
            party_data = zip(prt_name, prt_sym)
            election_data = {'election':election, 'party_data': party_data}
            return render(request, 'vote.html', election_data)

        else:
            return render(request,'not_eligible.html',{'error':'You are Not Eligible For This Voting Because Your State/District/Village is Different Than The Election Is being Held On!','link':'user_home'})

    else:
        return render(request, 'vote.html')

def isEligible(request,election):

    username = request.user.username
    voter = Voter.objects.get(pk = username)

    if (voter.state.upper() == election.state.upper() and voter.district.upper() == election.district.upper()):
        if (election.type_of_election == 'Sarpanch'):
            if(voter.village.upper() == election.village.upper() and voter.taluka.upper() == election.taluka.upper()):
                return True
            else:
                return False
        return True
    else:
        return False


@login_required(login_url = '/voting/')
def logout(request):
    auth.logout(request)
    return redirect('home')
