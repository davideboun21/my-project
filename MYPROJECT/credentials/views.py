from django.shortcuts import render
from django.http import HttpResponse
from .models import PersonalInformation, InstitutionsAttended


def homepage(request):
    personal_information = PersonalInformation.objects.all()
    institution_attended = InstitutionsAttended.objects.all()
    return render(request, 'homepage.html',
    {'personal_information' personal_information},
    {'institution_attended': institution_attended},
    )
