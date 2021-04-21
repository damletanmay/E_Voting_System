from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Election

# to get superuser id, password
def password(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('election_home')
        else:
            return render(request, 'election_login.html')
    else:
        superusers = list(User.objects.filter(is_superuser=True))
        username = request.POST.get("username")
        password = request.POST.get("password")
        # cheking if username is the first superuser
        if username == str(superusers[0]):
            user = auth.authenticate(username = username,password = password) # to get user
            if user is not None:
                auth.login(request,user)# for login.
                return redirect('election_home')
            else:
                # case where something is wrong!
                return render(request,'election_login.html',{'error':'Your Username or password is incorrect!'})
        else:
            # case where a simple user tries to login.
            return render(request,'election_login.html',{'error':'Authorized Personnel Only!'})


# to get data
def getData():
    election = Election.objects.filter(isOver = False)
    return election

# this page is for superusers only.
@login_required(login_url = '/election/password')
def election_home(request):
    if request.user.is_superuser:
        election_data = {'data': getData()}
        return render(request,'election_home.html',election_data);
    else:
        return HttpResponse("<h1> Authorized Personnel Only !</h1>")


@login_required(login_url = '/election/password')
def hold(request):
    if request.user.is_superuser:
        if request.method == 'GET': # for GET
            return render(request,'hold_election.html');

        elif request.method == 'POST': # for POST
        # cheking if data is not None
            if (request.POST.get('name') and
                request.POST.get('state') and
                request.POST.get('taluka') and
                request.POST.get('district') and
                request.POST.get('start') and
                request.POST.get('end') and
                request.POST.get('date')):

                # making a new election object to save in DB and eventually helding up an election
                election = Election()
                # getting & saving the data.
                election.name_of_election = request.POST.get('name')
                election.type_of_election = request.POST.get('type')
                election.state = request.POST.get('state')
                election.district = request.POST.get('district')
                election.taluka = request.POST.get('taluka')
                if request.POST.get('village'):
                    election.village = request.POST.get('village')
                else:
                    election.village = '-'
                if request.POST.get('city'):
                    election.city = request.POST.get('city')
                else:
                    election.city = '-'
                election.starting_time = request.POST.get('start')
                election.ending_time = request.POST.get('end')
                election.date = request.POST.get('date')
                election.isOver = False
                election.hold = request.user
                election.save()
                return render(request,'success.html',{'output':'Election Successfully Added!','smallop':'Election Added!','link':'election_home'})

            else:
                return render(request,'hold_election.html',{'error':'All Fields are Required !'})
    else:
        # case where a simple user tries to login.
        return HttpResponse("<h1> Authorized Personnel Only !</h1>")
