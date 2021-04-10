from django.shortcuts import render
from election.models import Election
from candidate.models import Candidate

def home(request):
    return render(request,'index.html')


def result(request):
    election = Election.objects.filter(isOver=True)
    return render(request, 'result.html',{'data':election})

def winner(request,election_id):
    election = Election.objects.get(pk= election_id)
    candidate = Candidate.objects.filter(election__id = election_id)
    nota_votes = election.NOTA_votes

    candidates_votes = []

    for x in candidate:
        candidates_votes.append(x.total_votes)

    max_votes = max(candidates_votes)

    #first
    winner = Candidate.objects.get(election__id = election_id,total_votes = max_votes)

    winner_name = winner.voter.getName()

    candidates_votes.remove(max(candidates_votes))
    second_votes = max(candidates_votes)
    second = Candidate.objects.get(election__id = election_id,total_votes = max_votes)

    candidates_votes.remove(max(candidates_votes))
    third_votes = max(candidates_votes)
    third = Candidate.objects.get(election__id = election_id,total_votes = max_votes)


    if max_votes > nota_votes:
        first = "Winner Of the Election: "+ election.name_of_election+" is "+winner_name+" with total " + str(max_votes)+ " votes"
        return render(request, 'winner.html',{'first':first,'second':second,'second_votes':second_votes,'third':third,'third_votes':third_votes})

    elif max_votes == nota_votes:

        first = 'NOTA and '+ winner_name + " are tied for the first place !"
        return render(request, 'winner.html',{'first':first,'second':second,'second_votes':second_votes,'third':third,'third_votes':third_votes})

    else:
        first = "NOTA has total votes =  " + str(nota_votes) + " and are the maximum number of votes."
        return render(request, 'winner.html',{'first':first,'second':winner,'second_votes':max_votes,'third':second,'third_votes':second_votes})
