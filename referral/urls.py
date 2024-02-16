from django.urls import path
from .views import *

app_name = 'referral'

urlpatterns = [
    path('referral_list/', referral_list, name='referral_list'),
    path('referral_create/', referral_create, name='referral_create'),
    path('create_patient/', create_patient, name='create_patient'),
    path('view_patients/', view_patients, name='view_patients'),
    path('create_hospital/', create_hospital, name='create_hospital'),
    path('view_hospitals/', view_hospitals, name='view_hospitals'),



]