# referrals/forms.py

from django import forms
from .models import Referral, Patient, Hospital, Disease


class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['patient', 'referred_to_hospital','referring_hospital', 'reason']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'location', 'gender', 'weight', 'id_number' ]

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['name', 'description']

