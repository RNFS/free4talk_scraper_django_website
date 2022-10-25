from django.urls import path

from . import views

app_name = "scraper"  

urlpatterns = [
    path("", views.index, name="index"),
    path('update-db', views.update_db, name='update_db'),
    path("search", views.search, name="search")

]