from email.policy import default
from django.db import models
import requests
from django.utils import timezone
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    followers = models.PositiveSmallIntegerField()
    following = models.PositiveSmallIntegerField()
    friends = models.PositiveSmallIntegerField()
    avatar_url = models.URLField()
    time = models.DateTimeField(default=timezone.now)



# the following part of the code it to update the data base by scraping the website "free4talk"
class JsonRequest():
    # this url will return json data including all info for online user 
    # like thier names and id and so on 
    __url = "https://free4talk-sync.herokuapp.com/sync/get/free4talk/groups/?a=sync-get-free4talk-groups"
    
    status = None
    
    # make a request and return the data as json data that python can handel
    @classmethod
    def get_json_data(cls):
        res =requests.post(cls.__url)
        res.encoding='utf-8-sig'
        cls.status = res.status_code
        return res.json()
    
    # just for returning the request status code 
    @classmethod
    def __str__(cls):
        return cls.status       

# this class will get the data recvived from the JsonRequest class as a param and then parse it 
# and also can save the data into the data base in scraper_user tabel
class ParsedData():
    
    def __init__(self, data):
        self.__data = data
        self.num_users = 0
    
    def save_data(self):
        # catch any exception occures during the processes and return false if anything goes wrong
        # so then views can return the right page or 500 page 
        try:
            for room in self.__data["data"]:
                for user in self.__data["data"][room]["clients"]:
                    # if user found then update his thier data
                    try:
                        x = User.objects.get(user_id=user["id"])
                        x.name = user["name"]
                        x.followers = user["followers"]
                        x.following = user["following"]
                        x.friends = user["friends"]
                        x.avatar = user["avatar"]
                        x.time=timezone.now()
                        x.save()
                    # if user not found then add it to the database                        
                    except User.DoesNotExist:                        
                        user_x = User(
                            name=user["name"], user_id=user["id"], followers=user["followers"], following=user["following"],
                            friends=user["friends"], avatar_url=user["avatar"], time=timezone.now()
                        )
                        user_x.save()
                        self.num_users += 1
                                           
            return True
        except (ValueError, KeyError): 
            return False 

    def __str__(self):     
        return F"{self.num_users}"