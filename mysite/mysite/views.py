from django.http import HttpResponse
from django.views import generic

class HomepageView(generic.ListView):
  queryset = []
  template_name = "index.html"

def index(request):
  return HttpResponse("This is the homepage of my site.")