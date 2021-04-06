from django.db import models

class Candidate(models.Model):

    voter_id = models.CharField(default = None,max_length = 30)
    election_id = models.CharField(default = None,max_length = 30)
    party_name = models.CharField(default = None,max_length = 30)
    party_logo = models.ImageField(upload_to = 'candidates/',default = None)
    party_motto = models.TextField(default = None,max_length = 200)
    party_leader_name = models.CharField(default = None,max_length = 30)
    total_votes = models.PositiveBigIntegerField()

    def __str__(self):
        return self.voter_id + self.election_id
