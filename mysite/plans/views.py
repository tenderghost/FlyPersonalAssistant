from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Plan


class IndexView(generic.ListView):
    template_name = "plans/index.html"
    context_object_name = "latest_plan_list"

    def get_queryset(self):
        return Plan.objects.all()


def index(request):
    return HttpResponse('Plan Management start here!')