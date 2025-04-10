from django.http import HttpResponse
from django.http import JsonResponse
from .models import CrimeRecord
import requests
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def get_crime_data(request):
    crime_data = CrimeRecord.objects.all()
    print(f"Crime data found: {crime_data}")  # Print to the console
    crime_list = list(crime_data.values("zipcode",  "total_crime"))
    print(f"Crime list: {crime_list}")  # Print the serialized data
    return JsonResponse(crime_list, safe=False)
