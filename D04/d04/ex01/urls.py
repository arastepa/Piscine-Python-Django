from django.urls import path
from .views import django, display, templates
urlpatterns = [
    path('django', django),
    path('display', display),
    path('templates', templates),
]