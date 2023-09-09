from django.urls import path
from .views import  populate, display

urlpatterns = [
    path('populate', populate),
    path('display', display),
]