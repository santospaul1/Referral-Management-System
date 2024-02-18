# referrals/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Referral, Patient, Hospital, Disease


class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['patient', 'referred_to_hospital','referring_hospital', 'reason', 'diseases']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'location', 'gender', 'weight', 'id_number' ]

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['name', 'description']

class HospitalForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    location = forms.CharField(max_length=50)
    level = forms.CharField(max_length=10, required=False)
    branches = forms.CharField(max_length=100, required=False)
    capacity = forms.IntegerField()

    diseases = forms.ModelMultipleChoiceField(queryset=Disease.objects.all(), required=False)

    class Meta:
        model = Hospital
        fields = ['email', 'password1', 'password2', 'name', 'location', 'level', 'branches', 'capacity', 'diseases']