from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import PeriodDef

# Create your views here.

class IndexView(generic.ListView):
    template_name = "periods/index.html"
    context_object_name = "period_defs"
    queryset = PeriodDef.objects.all()
    pass

def index(request):
    cnt = PeriodDef.objects.all().length()

    return HttpResponse("Hello from Periods! You have %d PeriodDef." % cnt)