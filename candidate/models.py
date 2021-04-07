from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):

    id = models.AutoField(primary_key=True)
    voter_id = models.CharField(default = None,max_length = 30)
    election_id = models.CharField(default = None,max_length = 30)
    party_name = models.CharField(default = None,max_length = 30)
    party_logo = models.ImageField(upload_to = 'images/candidates/')
    party_motto = models.TextField(default = None,max_length = 200)
    party_leader_name = models.CharField(default = None,max_length = 30)
    total_votes = models.PositiveBigIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.voter_id + self.election_id
