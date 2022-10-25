from wsgiref.validate import validator
from django.shortcuts import render
from django.http import HttpResponse

from . import models 

# Create your views here.
def update_db(request):
    data = models.JsonRequest.get_json_data()
    ob = models.ParsedData(data)
    if ob.save_data():
        new_users = ob.num_users 
        content = f"data stored in the database successfully, added {new_users} new users"
        return render(request, "scraper/update_db.html", {"content": content})
    return HttpResponse("503")        


def index(request):
    users_num = models.User.objects.count()
    return render(request, "scraper/index.html", {"users_num": users_num})