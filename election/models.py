from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Election(models.Model):
    id = models.AutoField(primary_key=True)
    type_of_election = models.CharField(default = None,max_length = 30);
    name_of_election = models.CharField(default = None,max_length = 100);
    state = models.CharField(default = None,max_length = 30);
    district = models.CharField(default = None,max_length = 30);
    taluka = models.CharField(default = None,max_length = 30);
    city = models.CharField(default = None,max_length = 30);
    village = models.CharField(default = None,max_length = 30);
    starting_time = models.TimeField(auto_now=False, auto_now_add=False)
    ending_time = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.DateField(default=None);
    hold = models.ForeignKey(User,on_delete=models.CASCADE)
    NOTA_votes = models.PositiveBigIntegerField(default=0)
    isOver = models.BooleanField(default = False)

    def __str__(self):
        return self.name_of_election

    def getTime(self):
        return str(self.starting_time) + '-' +str( self.ending_time)

    def getDate(self):
        return self.date.strftime('%d %B %Y')
