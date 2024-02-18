from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
# referral/views.py

from django.shortcuts import render, redirect
from .models import Referral, Patient, Hospital, Disease
from .forms import ReferralForm, PatientForm, DiseaseForm, HospitalForm


def referral_list(request):
    referrals = Referral.objects.all()
    return render(request, 'referrals/referral_list.html', {'referrals': referrals})

def referral_create(request):
    if request.method == 'POST':
        form = ReferralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('referral:referral_list')
    else:
        form = ReferralForm()
    return render(request, 'referrals/referral_form.html', {'form': form})

def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('referral:view_patients')
    else:
        form = PatientForm()
    return render(request, 'referrals/create_patient.html', {'form': form})

def view_patients(request):
    patients = Patient.objects.all()
    return render(request, 'referrals/view_patients.html', {'patients': patients})


def create_hospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # Log in the newly created user
            login(request, user)
            form.save_m2m()  # Save many-to-many relationships after saving the user
            return redirect('referral:view_hospitals')
    else:
        form = HospitalForm()

    return render(request, 'referrals/create_hospital.html', {'form': form})
def view_hospitals(request):
    hospitals = Hospital.objects.all()
    return render(request, 'referrals/view_hospitals.html', {'hospitals': hospitals})
def create_disease(request):
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('referral:view_diseases')
    else:
        form = DiseaseForm()
    return render(request, 'referrals/create_disease.html', {'form': form})
def view_diseases(request):
    diseases = Disease.objects.all()
    return render(request, 'referrals/view_diseases.html', {'diseases': diseases})
