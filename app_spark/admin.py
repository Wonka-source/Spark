from django.contrib import admin
from .models import Event

admin.site.register(Event)


# @admin.register(Event)
# class EventAdmin(Event):

#     prepopulated_fields = {'slug': ('title', 'when',)}
#     list_filter = ('venue', 'promoter')
#     list_display = ('venue', 'promoter', 'title', 'when')
#     search_fields = ('venue', 'promoter', 'title', 'when')


#     actions = ['approve_venue']


# @admin.register(Venue)
# class VenueAdmin(admin.ModelAdmen)

#     list_display = ('promoter', 'venue_name', 'venue_address', 'promoter_email')
#     list_filter = ('approved', 'submitted_on')
#     actions = ['approve_venue']

#     def approve_venue(self, request, queryset):
#         queryset.update(approved=True)
