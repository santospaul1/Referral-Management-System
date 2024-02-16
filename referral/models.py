# referral/models.py

from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)
class Hospital(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, default=None)
    name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=30, default=1024)
    location = models.CharField(max_length=50, default=None)
    level = models.CharField(max_length=10, null=True)
    branches = models.CharField(max_length=100, null=True)
    capacity = models.IntegerField(default=0)

    # Add more fields as needed

    def __str__(self):
        return self.name

class Patient(models.Model):

    first_name = models.CharField(max_length=30,default=None)
    last_name = models.CharField(max_length=30,default=None)
    id_number = models.IntegerField(null=True)
    location = models.CharField(max_length=30,default=None)
    weight = models.IntegerField(default=None)
    gender = models.CharField( max_length=10,
                               default=None,
                               choices=GENDER_CHOICES)
    admission_date = models.DateTimeField(auto_now_add=True)

    # Add more fields as needed

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

'''
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, default=None)

    # Add more fields as needed

    def __str__(self):
        return self.user.username
'''
class Referral(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    referring_hospital = models.ForeignKey(Hospital, related_name='referrals_sent', default=None, on_delete=models.CASCADE)
    referred_to_hospital = models.ForeignKey(Hospital, related_name='referrals_received', default=None, on_delete=models.CASCADE)
    #referring_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Referral for {self.patient} from {self.referring_hospital} to {self.referred_to_hospital}"

class Disease(models.Model):
    name = models.CharField(max_length=50, default=None)
    description = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.name