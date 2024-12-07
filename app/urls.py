from django.urls import path
from .views import *
urlpatterns = [
    path("admins/",admins, name="admins"), 
    path("register_unit/",register_unit, name="register_unit"),
]