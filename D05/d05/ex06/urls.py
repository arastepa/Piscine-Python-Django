from django.urls import path
from .views import init, populate, display, update

urlpatterns = [
    path('init', init),
    path('populate', populate),
    path('display', display),
    path('update', update),
]