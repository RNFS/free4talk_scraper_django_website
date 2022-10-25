from django import forms

class UserId(forms.Form):
    user_id = forms.CharField(max_length=200)

class UserName(forms.Form):
    name = forms.CharField(max_length=200)    