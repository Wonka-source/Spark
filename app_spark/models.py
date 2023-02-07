from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone

STATUS = ((0, 'Draft'), (1, "Post to All sparks"))


class Event(models.Model):
    title = models.CharField(max_length=200)
    promotion_company_name = models.CharField(max_length=200)
    promoter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="event_pages")
    image = CloudinaryField(blank=True, default="placeholder")
    where = models.CharField(max_length=250)
    when = models.DateTimeField(default=timezone.now)
    optional_end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-when']

    def __str__(self):
        return self.title
