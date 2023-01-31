from django.contrib import admin
from .models import Event


# admin.site.register(Event)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_filter = ('promoter', 'status', 'created_on')
    list_display = ('promotion_company_name', 'when', 'where', 'created_on', 'status')
