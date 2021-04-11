from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Voter
from election.models import Election
from candidate.models import Candidate
import datetime

# for login page.
# As there are two types of requests GET & POST i checked where to redirect if either was the case in each view.


def login(request):

    if request.method == 'GET':# for GET request to this view.
        if request.user.is_authenticated: # checking if user is logged in .
            return redirect('user_home') # redirecting to the home page, so that user don't need to log in again
        else:
            # However, if he is not logged in then login page will be showned to him.
            return render(request, 'login.html')

    elif request.method == 'POST':# for POST request to this view.
        superusers = list(User.objects.filter(is_superuser=True)) # getting superusers
        username = request.POST.get("voter_id")# getting voter_id

        if username == str(superusers[0]): # checking if username is equal to first superuser
            return redirect('password') # if yes then, redirecting to the admin side of the page.
        else:

            '''

            for authentication i've used a system,
             where if you are a voter i.e. if your data does exist in the Database,
             then for the first time you login, your account will be made and from then onwards
             you will directly login into the website.
             i've not created the sign-up page for this, because it does not make sense realted to this context,
             as if we Already have a voter-id then we should be authenticated & making a sign-up page wouldn't be logical.

             '''

            if(username is not None):
                try:
                    voter = Voter.objects.get(pk = username) # error will be raised if no such voter is found.
                    user = auth.authenticate(username = username,password = username) # to check if the voter Already has an account.
                    # if the voter does have an account it will return the user and log him in.
                    # else it will create an account for the voter and then log user in.

                    if user is not None:
                        auth.login(request,user) # used to login
                        return redirect('user_home')
                    else:
                        user = User.objects.create_user(username,password = username)
                         # to make user
                        auth.login(request,user)
                        election_data = {'data': getData()}
                        return redirect('user_home')

                except Voter.DoesNotExist:# above error will be handled here.
                    return render(request, 'login.html',{'error':"Invalid Voter Id"})


# to get such elections from database which are not yet over.
def getData():
    election = Election. objects.filter(isOver = False)
    return election


# this is to render home url directly if someone is Already logged in.
@login_required(login_url = '/voting/') # this will redirect to login page if user is not authenticated
def user_home(request):
    election_data = {'data': getData()}
    return render(request, 'user_home.html', election_data)


# this is to display the voter id card to the website.
@login_required(login_url = '/voting/') # this will redirect to login page if user is not authenticated
def user_profile(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username # to get username
        ''' now the next line works because, while creating an account for the voters
            i stored thier voting number as username, so due to this it will return
             all the information/object for the particular voting number which can
             be displayed to the web page.
         '''
        voter = Voter.objects.get(pk = username)
        return render(request, 'user_profile.html', {'voter':voter})


@login_required(login_url = '/voting/') # this will redirect to login page if user is not authenticated
def vote(request,election_id):
    if request.method == 'GET':# for GET request

        election =  Election.objects.get(pk = election_id) # getting particular election user clicked on.
        now =  datetime.datetime.now() # getting time.

        # checking if the date is same as election date.
        if (now.day == election.date.day and now.month == election.date.month and now.year == election.date.year ):
            # checking if time is between the election time.
            if (now.hour <= election.starting_time.hour and now.minute <= election.starting_time.minute):
                # case where user is early.
                return render(request,'not_eligible.html',{'error':'Election has not Started Yet!','link':'user_home'})

            elif (now.hour >= election.ending_time.hour and now.minute >= election.ending_time.minute):
                #case where user is late.
                '''
                 here if any user tries to access the election, only for that user, it'll redirect to below page.
                 once any user clicks to vote ... election status will flick and election will end
                 i.e. in database isOver paramater becomes true
                 which is why if you go again to the home page, you will not see that election thier.
                '''
                election.isOver = True
                election.save()
                return render(request,'not_eligible.html',{'error':'Election has Ended!','link':'user_home'})

            else: # case where user is in given date & time.

                if isEligible(request,election): # checking for eligibilty criteria.

                    # checking if user already has voted.
                    if hasNotVoted(request,request.user.username,election_id):
                        candidate_data = getCandidateData(election_id) # getting data.
                        return render(request, 'vote.html', candidate_data)

                    else:# case where user is already voted.
                        return render(request,'not_eligible.html',{'error':'You Already Have Voted !','link':'user_home'})

                else:# case where user lives elsewhere & clicks to vote in other election.
                    return render(request,'not_eligible.html',{'error':'You are Not Eligible For This Voting Because Your State/District/Village is Different Than The Election Is being Held On!','link':'user_home'})
        else: # case where user did not visit this page on the same date.
            return render(request,'not_eligible.html',{'error':'Election is on '+ str(election.date.strftime('%d -''%m -''%Y')),'link':'user_home'})

    else:# for POST request

        # getting candidate id so that we can incerement thier vote.
        user_vote = request.POST.get('user_vote')

        # getting user
        get_voter = request.POST.get('voter')

        if user_vote is not None:
            # getting voter so that we can add election id to the list of voted elections
            voter = Voter.objects.get(pk = get_voter)
            voter.voted_elections.append(election_id)
            voter.save()

            if user_vote == 'NOTA': # case where user voted for NOTA
                ''' in this case i will incerement the election db's NOTA_votes Field
                    i've kept this field in genral because NOTA  does not represnt any party. '''

                election = Election.objects.get(pk = election_id)
                election.NOTA_votes +=1
                election.save()
            else:
                ''' incerementing the candidate's total_votes when user votes for a candidate
                    rather than voting in nota '''
                candidate = Candidate.objects.get(pk = user_vote)
                candidate.total_votes+=1
                candidate.save()
            return render(request,'success.html',{'output':'Successfully Voted!','link':'user_home'})

        else:
            '''  Case where user forgets a field to Select, but this won't probably happen,
                 as i have added reqired attribute to the input field '''
            return render(request,'vote.html',{'error':'Select A Field To Vote!'})

# to get candidate data for different elections.
def getCandidateData(elec_id):

    candidates = Candidate.objects.filter(election__id = elec_id)
    election = Election.objects.get(pk = elec_id)
    candidate_data = {'candidates':candidates,'election':election}

    return candidate_data

# checking if user is Eligible to vote
# i.e. if the user's data matches the election's date where it is held.
def isEligible(request,election):

    username = request.user.username
    voter = Voter.objects.get(pk = username)

    if (voter.state.upper() == election.state.upper() and voter.district.upper() == election.district.upper() and voter.taluka.upper() == election.taluka.upper()):
        if (election.type_of_election == 'Sarpanch'):
            if(voter.village.upper() == election.village.upper() and voter.taluka.upper() == election.taluka.upper()):
                return True
            else:
                return False
        return True
    else:
        return False

# checking if user has not voted.
def hasNotVoted(request,voter_id,election_id):
    voter = Voter.objects.get(pk = voter_id)

    if election_id in voter.voted_elections:
        return False
    else:
        return True

# logout
@login_required(login_url = '/voting/')
def logout(request):
    auth.logout(request)
    return redirect('home')
