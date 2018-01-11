from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic
from django.http import HttpResponse
from .models import Plan


class IndexView(generic.ListView):
    template_name = "plans/index.html"
    context_object_name = "latest_plan_list"

    def get_queryset(self):
        return Plan.objects.all()


class CreateView(generic.CreateView):
    template_name = "plans/create.html"
    fields = ['plan_text', 'category', 'start_date', 'end_date']
    model = Plan


def index(request):
    return HttpResponse('Plan Management start here!')