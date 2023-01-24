from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, "Post to All sparks"))


# class Venue(models.Model):
#     name = models.CharField(max_length=250)
#     address = models.TextField(max_length=800)

class Event(models.Model):
    title = models.CharField(max_length=250)
    # slug = modeles.SlugField(max_length=300, unique=True)
    # promoter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_posts")
    image = CloudinaryField(blank=True, default="placeholder")
    venue = models.CharField(max_length=250)
    address = models.TextField(max_length=800)
    when = models.DateTimeField()
    description = models.TextField(blank=True)
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-when']

    def __str__(self):
        return self.title
