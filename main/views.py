from django.shortcuts import render
from .models import PersonalComputer


def index(request):
    pcs = PersonalComputer.objects.all

    return render(request, 'main/index.html',
                  {
                      'pcs': pcs
                  })
