from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tip(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name="upvoted_tips", blank=True)
    downvotes = models.ManyToManyField(User, related_name="downvoted_tips", blank=True)