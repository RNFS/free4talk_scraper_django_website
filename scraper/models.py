from django.db import models
import requests


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    followers = models.PositiveSmallIntegerField()
    following = models.PositiveSmallIntegerField()
    friends = models.PositiveSmallIntegerField()
    avatar_url = models.URLField()




class JsonRequest():

    __url = "https://free4talk-sync.herokuapp.com/sync/get/free4talk/groups/?a=sync-get-free4talk-groups"
    
    status = None
    
    @classmethod
    def get_json_data(cls):
        res =requests.post(cls.__url)
        res.encoding='utf-8-sig'
        cls.status = res.status_code
        return res.json()
    
    @classmethod
    def __str__(cls):
        return cls.status       


class ParsedData():
    
    def __init__(self, data):
        self.__data = data
        self.num_users = 0
    
    def save_data(self):
        try:
            for room in self.__data["data"]:
                for user in self.__data["data"][room]["clients"]:
                    try:
                        User.objects.get(user_id=user["id"])
                    
                    except User.DoesNotExist:                        
                        user_x = User(
                            name=user["name"], user_id=user["id"], followers=user["followers"], following=user["following"],
                            friends=user["friends"], avatar_url=user["avatar"]
                        )
                        user_x.save()
                                           
            return True
        except (ValueError, KeyError): 
            return False 

    def __str__(self):     
        return F"{self.num_users}"