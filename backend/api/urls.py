from django.urls import path
from . import views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("data", views.get_crime_data, name="crime_data"),
]