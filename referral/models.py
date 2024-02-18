# referral/models.py
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

class Disease(models.Model):
    name = models.CharField(max_length=50, default=None)
    description = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.name


class MyHospitalManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Hospital(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=50)
    level = models.CharField(max_length=10, null=True)
    branches = models.CharField(max_length=100, null=True)
    diseases = models.ManyToManyField('Disease', null=True)
    capacity = models.IntegerField(default=0)

    # Add more fields as needed

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyHospitalManager()

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
    diseases = models.ManyToManyField('Disease', null=True)

    def __str__(self):
        return f"Referral for {self.patient} from {self.referring_hospital} to {self.referred_to_hospital}"

