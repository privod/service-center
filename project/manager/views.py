from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext

from manager.models import Atm


def index(request):
    atm_list = Atm.objects.all()
    context = {'atm_list': atm_list}
    return render(request, 'manager/index.html', context)
