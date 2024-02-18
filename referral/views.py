from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
# referral/views.py

from django.shortcuts import render, redirect
from .models import Referral, Patient, Hospital, Disease
from .forms import ReferralForm, PatientForm, DiseaseForm


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
        # Extract form data
        email = request.POST.get('email')
        username = email  # Assuming email as username
        password = request.POST.get('password')
        name = request.POST.get('name')
        location = request.POST.get('location')
        level = request.POST.get('level')
        branches = request.POST.get('branches')
        capacity = request.POST.get('capacity')
        diseases = request.POST.get('diseases')

        # Create user instance
        user = User.objects.create_user(username=username, email=email, password=password, diseases=diseases)

        # Create hospital instance
        hospital = Hospital.objects.create(user=user, email=email, name=name, location=location, level=level, branches=branches, capacity=capacity)

        # Redirect to a success page or any other view
        return redirect('referral:view_hospitals')  # Change 'success_url' to your desired URL name

    # If the request method is GET, render the form
    return render(request, 'referrals/create_hospital.html')
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
