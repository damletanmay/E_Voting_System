from django.db import models

class  Voter(models.Model):

    voting_number = models.CharField(max_length = 20,default = None,primary_key = True)
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

    def __str__(self):
        return self.voting_number

    def getName(self):
        return (self.fname + ' ' + self.mname + ' ' + self.lname)

    def getDOB(self):
        return str(self.dob)
