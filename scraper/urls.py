from django.urls import path

from . import views

urlpatterns = [
    path('update-db', views.update_db, name='update_db'),
]