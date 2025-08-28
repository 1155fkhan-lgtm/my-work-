from django.urls import path
from . import views

urlpatterns = [
    path('', views.picture_list, name='picture_list'),
]