from django.db import models
from django.utils import timezone

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True, null=False)
    episode_nb = models.PositiveIntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)

    created = models.DateTimeField(default=timezone.now, editable=False)
    updated = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        # Automatically update the 'updated' field with the current date and time
        self.updated = timezone.now()
        super(Movies, self).save(*args, **kwargs)


    def __str__(self):
        return self.title