from django.shortcuts import render,redirect,HttpResponse
from users.models import Voter
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from election.models import Election

# Create your views here.
def candidate_login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('candidate_voter')
        else:
            return render(request, 'candidate_login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username is not None:
            superusers = list(User.objects.filter(is_superuser=True))
            username = request.POST.get("username")
            password = request.POST.get("password")

            if username == str(superusers[0]):
                user = auth.authenticate(username = username,password = password)
                if user is not None:
                    auth.login(request,user)
                    return redirect('candidate_voter')
                else:
                    return render(request,'candidate_login.html',{'error':'Your Username or password is incorrect!'})
            else:
                return render(request,'candidate_login.html',{'error':'Authorized Personnel Only!'})


@login_required(login_url = '/candidate/')
def candidate_voter(request):
    if request.method == 'GET':
        if request.user.is_superuser:
            return render(request,'getId.html')
        else:
            return HttpResponse("Authorized Personnel Only !")
    else:
        return redirect('candidate_voter')


@login_required(login_url = '/candidate/')
def candidate_home(request):
    if request.method == 'GET':
        if request.user.is_superuser:
            return redirect('candidate_voter')
        else:
            return HttpResponse("Authorized Personnel Only !")
    else:
        voter_id = request.POST.get("voter_id")
        try:
            voter = Voter.objects.get(pk = voter_id)
            election = Election.objects.all()
            return render(request,'candidate_home.html',{'elections':election,'voter':voter})
        except Voter.DoesNotExist:
            return render(request,'getId.html',{'error':'Invalid Voter Id!'})


@login_required(login_url = '/candidate/')
def candidate_register(request,election_id,voter_id):
    if request.method == 'GET':
        if request.user.is_superuser:
            if isEligible(election_id,voter_id):
                return render(request,'register.html')
            else:
                return render(request,'not_eligible.html',{'error':'You are Not Eligible For Candidacy in This Election Because Your State/District/Village is Different Than The Election Is being Held On!','link':'candidate_home'})
        else:
            return HttpResponse("Authorized Personnel Only !")
    else:
        return render(request,'register.html')


def isEligible(election_id,voter_id):
    election = Election.objects.get(pk = election_id)
    voter = Voter.objects.get(pk = voter_id)

    if (voter.state.upper() == election.state.upper() and voter.district.upper() == election.district.upper()):
        if (election.type_of_election == 'Sarpanch'):
            if(voter.village.upper() == election.village.upper() and voter.taluka.upper() == election.taluka.upper()):
                return True
            else:
                return False
        return True
    else:
        return False

@login_required(login_url = '/candidate/')
def logout(request):
    auth.logout(request)
    return redirect('candidate_login')
