from django.urls import path
from .views import init, populate, display, remove

urlpatterns = [
    path('init', init),
    path('populate', populate),
    path('display', display),
    path('remove', remove),
]