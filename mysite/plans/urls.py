from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'plans'
urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='index'),
    path('create/', views.CreateView.as_view(), name='create')
]