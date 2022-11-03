from wsgiref.validate import validator
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from . import models 
from .forms import UserId, UserName


# Create your views here.
def update_db(request):
    data = models.JsonRequest.get_json_data()
    ob = models.ParsedData(data)
    if ob.save_data():
        users_num = models.User.objects.count()
        return render(request, "scraper/update_db.html", {"new_users": ob.num_users, "users_updated":users_num})
    return HttpResponse("503")        


def index(request):
    users_num = models.User.objects.count()
    return render(request, "scraper/index.html", {"users_num": users_num})


def search(request):
    if request.method == "POST":
        user_id, user_name = UserId(request.POST), UserName(request.POST)
    
        if user_id.is_valid() and user_name.is_valid():
            user_id, user_name = user_id.cleaned_data, user_name.cleaned_data
            user_id, user_name = user_id["user_id"], user_name["name"]

            try:
                user = models.User.objects.get(Q(name=user_name) & Q(user_id=user_id)) 
                return render(request, "scraper/res.html", {"user_data": user})
            
            except(models.User.DoesNotExist, TypeError):
                
                try:
                    users = models.User.objects.filter(Q(name=user_name) | Q(user_id=user_id)) 
                    return render(request, "scraper/res.html", {"users": users})
                
                except(models.User.DoesNotExist, TypeError):                    
                    return HttpResponse("404 User Not Found")
                            
        else:
            return render(request, "scraper/search.html", {"user_id":UserId, "user_name": UserName})

    return render(request, "scraper/search.html", {"user_id":UserId, "user_name": UserName})        



def delete(request):
    ...
    #TODO

def reg(request):
    if request.method == "POST":
        ...
        
    return render(request, "reg.html")    
