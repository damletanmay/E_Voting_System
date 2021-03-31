from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Election

def getData():
    election = Election. objects.all()
    return election

@login_required(login_url = '/election/password')
def election_home(request):
    if request.user.is_superuser:
        election_data = {'data': getData()}
        return render(request,'election_home.html',election_data);
    else:
        return HttpResponse("Authorized Personnel Only !")


@login_required(login_url = '/election/password')
def hold(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            return render(request,'hold_election.html');
        elif request.method == 'POST':
            if (request.POST.get('name') and
                request.POST.get('state') and
                request.POST.get('taluka') and
                request.POST.get('city') and
                request.POST.get('district') and
                request.POST.get('start') and
                request.POST.get('end') and
                request.POST.get('date')):

                election = Election()
                election.name_of_election = request.POST.get('name')
                election.type_of_election = request.POST.get('type')
                election.state = request.POST.get('state')
                election.district = request.POST.get('district')
                election.taluka = request.POST.get('taluka')
                election.city = request.POST.get('city')
                if request.POST.get('village'):
                    election.village = request.POST.get('village')
                else:
                    election.village = '-'
                election.starting_time = request.POST.get('start')
                election.ending_time = request.POST.get('end')
                election.date = request.POST.get('date')

                election.hold = request.user
                election.save()
                return redirect('election_home')

            else:
                return render(request,'hold_election.html',{'error':'All Fields Required !'})
    else:
        return HttpResponse("Authorized Personnel Only !")


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

        if username == str(superusers[0]):
            user = auth.authenticate(username = username,password = password)
            if user is not None:
                auth.login(request,user)
                return redirect('election_home')
            else:
                return render(request,'election_login.html',{'error':'Your Username or password is incorrect!'})
        else:
            return render(request,'election_login.html',{'error':'Authorized Personnel Only!'})
