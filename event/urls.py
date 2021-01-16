from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [

    path('',views.Homepage),
    path('Base',views.Homepage,name='Homepage'),
    path('ParticipantRegistration/',views.ParticipantRegistration, name='PR'),
    path('Eventregistration/',views.EventReg, name='ER'),
    path('Eventdashboard/',views.EventDashboard, name='ED'),
    path('form/',views.form),

]
