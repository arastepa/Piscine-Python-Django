from django.urls import path
from .views import  populate, display, update

urlpatterns = [
    path('populate', populate),
    path('display', display),
    path('update', update),
]