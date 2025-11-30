from django.urls import path
from . import views

app_name = 'app_analyst'

urlpatterns = [
    path("", views.Analyst.as_view(), name='analyst')
]
