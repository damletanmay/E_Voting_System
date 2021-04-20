from django.shortcuts import render
from election.models import Election
from candidate.models import Candidate

# to get the home page.
def home(request):
    return render(request,'index.html')

# to  get result page
def result(request):
    election = Election.objects.filter(isOver=True)
    return render(request, 'result.html',{'data':election})

# to get winner page.
def winner(request,election_id):
    # getting particular election and all candidates for that election.
    election = Election.objects.get(pk= election_id)
    allcandidate = Candidate.objects.filter(election__id = election_id).order_by('-total_votes')[1:] # __ in query indacates foreign key.
    nota_votes = election.NOTA_votes
    winner = Candidate.objects.filter(election__id = election_id).order_by('-total_votes')[0:1]
    print(winner[0])
    return render(request,'winner.html',{'allcandidates':allcandidate,'winner':winner,'nota_votes':nota_votes})
