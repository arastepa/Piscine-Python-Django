from django.urls import path
from .views import  populate, display, remove

urlpatterns = [
    path('populate', populate),
    path('display', display),
    path('remove', remove),
]