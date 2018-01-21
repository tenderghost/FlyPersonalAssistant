from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic
from django.http import HttpResponse
from .models import Plan


class IndexView(generic.ListView):
    template_name = "plans/index.html"
    context_object_name = "latest_plan_list"

    def get_queryset(self):
        req_params = self.request.GET

        if 'type' in req_params:
            # get request filters
            plan_type = self.request.GET['type']
            if plan_type == 'in_progress':
                return Plan.objects.filter(status = 'I').order_by("-end_date")
            elif plan_type == 'not_start':
                return Plan.objects.filter(status = 'U').order_by("-end_date")
            elif plan_type == 'finished':
                return Plan.objects.filter(status = 'F').order_by("-end_date")
            elif plan_type == 'all':
                return Plan.objects.all().order_by("-end_date")
        else:
            # no request parameter, set default view
            return Plan.objects.exclude(status='F').order_by("-end_date")



class CreateView(generic.CreateView):
    template_name = "plans/create.html"
    fields = ['plan_text', 'category', 'start_date', 'end_date']
    model = Plan


def index(request):
    return HttpResponse('Plan Management start here!')