from django.shortcuts import render

def login(request):
    return render(request, 'login.html')


def user_home(request):
    el_date = ['27/02/2021', '28/02/2021']
    el_name = ['17th Loksabha Election', '18th Loksabha Election']
    el_time = ['8:00 - 17:00 (IST)', '8:00 - 17:00 (IST)']

    data = zip(el_date, el_name, el_time)

    election_data = {'data': data}

    return render(request, 'user_home.html', election_data)


def user_profile(request):
    name = 'Yash Kavaiya'
    DOB = '2002-03-04'
    contact = '+91 00000 00000'
    vote_id = 'XXXXXXXXXX'

    user_values = {'name': name, 'dob': DOB, 'contact': contact, 'voting_id': vote_id}

    return render(request, 'user_profile.html', user_values)


def vote(request):
    prt_name = ['Narendra Modi', 'Rahul Gandhi']
    prt_sym = ['BJP', 'NCI']

    party_data = zip(prt_name, prt_sym)

    election_data = {'name': '17th Loksabha Election', 'party_data': party_data}
    
    return render(request, 'vote.html', election_data)

