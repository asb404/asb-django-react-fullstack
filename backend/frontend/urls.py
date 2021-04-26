from django.urls import path
from . import views
from frontend import views
urlpatterns = [
    path('', views.index),
    path("adduser/",views.adduser,name='adduser'),
]