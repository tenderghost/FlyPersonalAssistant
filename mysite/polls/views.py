from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello man, you are at polls index page.")
