from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_filter = ("promoter", "status", "created_on", "when")
    list_display = (
        "promoter",
        "created_on",
        "title",
        "promotion_company_name",
        "where",
        "when",
        "status")
