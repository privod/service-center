from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from manager.models import Atm


# Устаревший метод
def index(request):
    atm_list = Atm.objects.all()
    context = {'atm_list': atm_list}
    return render(request, 'manager/atm_list.html', context)


class AtmListView(ListView):
    model = Atm


class CreateAtmView(CreateView):
    model = Atm
    fields = [
        'ref',
        'serial',
        'number',
        'producer',
        'model',
        'city',
        'address',
    ]

    def get_success_url(self):
        return reverse('atm-list')