from django.urls import path
from .views import  home, delete_tip, profile, login, register, logout, upvote_tip, downvote_tip

urlpatterns = [
    path('', home, name = 'home'),
    path('login', login, name = "login"),
    path('register', register, name = "register"),
    path('logout', logout, name = "logout"),
    path('profile', profile, name = "profile"),
    path('tip/<int:tip_id>/upvote/',upvote_tip, name='upvote_tip'),
    path('tip/<int:tip_id>/downvote/',downvote_tip, name='downvote_tip'),
    path('tip/<int:tip_id>/delete/', delete_tip, name='delete_tip'),
]