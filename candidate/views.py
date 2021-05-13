from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Voter
from election.models import Election
from .models import Candidate
import datetime
# for loging into the panel superuser acc. is Required.
def candidate_login(request):

    if request.method == 'GET': # for get

        if request.user.is_authenticated:
            return redirect('candidate_voter')
        else:
            #case wher user is not already logged in.
            return render(request, 'candidate_login.html')

    else: # for POST request

        username = request.POST.get('username')
        password = request.POST.get('password')
        # login logic if it is a superuser

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
                    # case where something is wrong.
                    return render(request,'candidate_login.html',{'error':'Your Username or password is incorrect!'})
            else:
                # case when some simple user tries to login.
                return render(request,'candidate_login.html',{'error':'Authorized Personnel Only!'})

# for getting voter id of the user.
@login_required(login_url = '/candidate/')
def candidate_voter(request):
    if request.method == 'GET':
        if request.user.is_superuser:
            return render(request,'getId.html')
        else:
            return HttpResponse("<h1> Authorized Personnel Only !</h1>")
    else:
        return redirect('candidate_voter')


# for displaying the home page.
@login_required(login_url = '/candidate/')
def candidate_home(request):

    if request.method == 'GET':# for GET request

        if request.user.is_superuser:
            # it will redirect to voter page to get id.
            return redirect('candidate_voter')
        else:
            return HttpResponse("<h1> Authorized Personnel Only !</h1>")

    else: # for POST request
        # only way to GET this page is through a POST request in candidate_voter's template
        # i have done this Because id is needed .
        voter_id = request.POST.get("voter_id")
        try:
            # Exception will raise error if None is returned.
            voter = Voter.objects.get(pk = voter_id)
            # only getting such elections which are not over yet !
            election = Election.objects.filter(isOver = False)
            return render(request,'candidate_home.html',{'elections':election,'voter':voter})

        except Voter.DoesNotExist:# this will handle the above error
            return render(request,'getId.html',{'error':'Invalid Voter Id!'})


@login_required(login_url = '/candidate/')
def candidate_register(request,election_id,voter_id):

    if request.method == "POST": # for POST request.

        # getting files, checking if they exist , and saving into DB.
        party_name = request.POST['party_name']
        party_leader_name = request.POST['party_leader_name']
        party_motto = request.POST['party_motto']

        if party_name and party_leader_name and party_motto and request.FILES['party_symbol']:

            candidate = Candidate()
            candidate.voter = Voter.objects.get(pk=voter_id)
            candidate.election = Election.objects.get(pk = election_id)
            candidate.party_name = party_name
            candidate.party_leader_name = party_leader_name
            candidate.party_motto = party_motto
            candidate.party_logo = request.FILES['party_symbol']
            print(request.FILES['party_symbol'])
            candidate.total_votes = 0
            candidate.user = request.user
            candidate.save()
            return render(request,'success.html',{'output':'Successfully Registered into Election!','link':'candidate_home','smallop':'Registered'})

        else:
            return render(request,'register.html',{'error':"All Fileds Required!"})

    elif request.method == 'GET': # for GET request

        if request.user.is_superuser: # to check if user is a super user
            now =  datetime.datetime.now() # getting time.
            election =  Election.objects.get(pk = election_id)
            # checking if the date is same as election date.
            if (now.day < election.date.day and now.month <= election.date.month and now.year <= election.date.year ):
                # case where candidate isn't late for standing in election
                if isEligible(election_id,voter_id): # to check if user is Eligible

                    if isNotRegistered(election_id,voter_id): # to check if he is already Registered.

                        voter = Voter.objects.get(pk = voter_id)
                        election = Election.objects.get(pk=election_id)

                        return render(request,'register.html',{'voter':voter,'election':election})

                    else: # case where user is already registered.
                        return render(request,'not_eligible.html',{'error':'You already are Registered in this Election!','link':'candidate_home'})

                else: # case where user is not eligible.
                    return render(request,'not_eligible.html',{'error':'You are Not Eligible For Candidacy in This Election Because Your State/District/Village is Different Than The Election Is being Held On!','link':'candidate_home'})
            else:
                return render(request,'not_eligible.html',{'error':'Registrations Are Over!','link':'candidate_home'})
        else:
            # case when simple user tries to login.
            return HttpResponse("<h1> Authorized Personnel Only !</h1>")

# to check if user is eligible.
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

# to check if voter is already registerd in election.
def isNotRegistered(election_id,voter_id):
    try:
        candidate = Candidate.objects.get(election__id = election_id,voter__voting_number = voter_id)
        return False
    except Candidate.DoesNotExist:
            return True

# for logout
@login_required(login_url = '/candidate/')
def logout(request):
    auth.logout(request)
    return redirect('candidate_login')
