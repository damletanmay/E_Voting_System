from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Voter
from election.models import Election
from .models import Candidate


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
    if request.method == "POST":

        party_name = request.POST['party_name']
        party_leader_name = request.POST['party_leader_name']
        party_motto = request.POST['party_motto']

        if party_name and party_leader_name and party_motto and request.FILES['party_symbol']:

            candidate = Candidate()
            candidate.voter_id = voter_id
            candidate.election_id = election_id
            candidate.party_name = party_name
            candidate.party_leader_name = party_leader_name
            candidate.party_motto = party_motto
            candidate.party_logo = request.FILES['party_symbol']
            candidate.total_votes = 0
            print(candidate.voter_id)
            print(candidate.election_id)
            print(candidate.party_name)
            print(candidate.party_leader_name)
            print(candidate.party_motto)
            candidate.save()
            print(voter_id)
            print(election_id)
            return redirect('candidate_login')
        else:
            return render(request,'register.html',{'error':"All Fileds Required!"})

    elif request.method == 'GET':
        if request.user.is_superuser:
            if isEligible(election_id,voter_id):
                voter = Voter.objects.get(pk = voter_id)
                election = Election.objects.get(pk=election_id)
                return render(request,'register.html',{'voter':voter,'election':election})
            else:
                return render(request,'not_eligible.html',{'error':'You are Not Eligible For Candidacy in This Election Because Your State/District/Village is Different Than The Election Is being Held On!','link':'candidate_home'})
        else:
            return HttpResponse("Authorized Personnel Only !")


def isEligible(election_id,voter_id):
    election = Election.objects.get(pk = election_id)
    voter = Voter.objects.get(pk = voter_id)

    if (voter.state.upper() == election.state.upper() and voter.district.upper() == election.district.upper() and voter.taluka.upper() == election.taluka.upper()):
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
