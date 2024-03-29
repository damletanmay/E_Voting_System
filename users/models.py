from django.db import models
from django_mysql.models import ListTextField

class  Voter(models.Model):
    # this is the general information for all the voters which will be saved into database.
    voting_number = models.CharField(max_length = 20,default = None,primary_key = True)
    # upload_to will upload to the specified path for a media directory specified in settings.py
    user_img = models.ImageField(upload_to = 'images/voters/',default = None)
    fname = models.CharField(max_length = 20,default = None)
    mname = models.CharField(max_length = 20,default = None)
    lname = models.CharField(max_length = 20,default = None)
    phone_no = models.CharField(max_length = 10,default = None)
    city = models.CharField(max_length = 15,default = None)
    district = models.CharField(max_length = 15,default = None)
    state = models.CharField(max_length = 15,default = None)
    village = models.CharField(max_length = 15,default = None)
    taluka = models.CharField(max_length = 15,default = None)
    address = models.TextField(default = None)
    dob = models.DateField(default= None)
    # ListTextField comes from an different module.
    voted_elections =  ListTextField(
        blank = True,
        default = [],
        base_field=models.IntegerField(),
        size=1000,
    )

    # returns voting number
    def __str__(self):
        return self.voting_number

    # method which will return full name of the voter
    def getName(self):
        return (self.fname + ' ' + self.mname + ' ' + self.lname)

    # method to get DOB
    def getDOB(self):
        return str(self.dob)
