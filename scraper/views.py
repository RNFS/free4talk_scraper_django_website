from wsgiref.validate import validator
from django.shortcuts import render
from django.http import HttpResponse

from . import models 

# Create your views here.
def update_db(request):
    data = models.JsonRequest.get_json_data()
    ob = models.ParsedData(data)
    if ob.save_data():
        return HttpResponse("data stored in the database successfully")
    return HttpResponse("503")        