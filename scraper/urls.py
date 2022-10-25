from django.urls import path

from . import views

app_name = "scraper"  

urlpatterns = [
    path('update-db', views.update_db, name='update_db'),
    path("index", views.index, name="index")
]