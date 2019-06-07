from django.shortcuts import render
from appointment.forms.reception import ReceptionForm


def receprion(req):
    return render(req, 'reception.html', context={'form': ReceptionForm})
