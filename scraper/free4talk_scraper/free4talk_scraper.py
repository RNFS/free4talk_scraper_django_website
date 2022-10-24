import requests
from ..models import User


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
    
    def __init__(self):
        self.__data = JsonRequest.get_json_data()
        self.status = JsonRequest.status
        self.num_users = 0
    
    def save_data(self):
        try:
            for room in self.__data["data"]:
                for user in self.__data["data"][room]["clients"] :
                    self.num_users += 1
                    User.name = user["name"]
                    User.id = user["id"]
                    User.followers = user["followers"]
                    User.following = user["following"]
                    User.friends = user["friends"]
                    User.avatar_url = user["avatar"]
                    User.save()
            return True
        except: 
            return False 
    def __str__(self):     
        return F"{self.num_users}"

def driver():
    data = ParsedData()
    if data.status == 200:
        if checker := data.save_data():
            return "OK"
    return "False"

if __name__ == "__main__" :
    print(driver())
