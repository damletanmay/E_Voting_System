from django.db import models
from django.contrib.auth.models import User
from users.models import Voter
from election.models import Election

class Candidate(models.Model):
    # this class will save the candidates for particular election.

    id = models.AutoField(primary_key=True)
    election = models.ForeignKey(Election,on_delete=models.CASCADE,default=None) # ForeignKey Reference to election
    party_name = models.CharField(default = None,max_length = 30)
    # upload_to will upload the coming data to the specifed media folder in settings.py
    party_logo = models.ImageField(upload_to = 'images/candidates/')
    party_motto = models.TextField(default = None,max_length = 200)
    party_leader_name = models.CharField(default = None,max_length = 30)
    total_votes = models.PositiveBigIntegerField(default=0)
    voter = models.ForeignKey(Voter,on_delete = models.CASCADE,default=None) # ForeignKey Reference to voter
    user = models.ForeignKey(User,on_delete=models.CASCADE) # ForeignKey Reference to user

    def __str__(self):
        return str(self.id)
