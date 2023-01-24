from django import forms
from .models import Event
from django.contrib.admin.widgets import AdminSplitDateTime


class EventForm(forms.ModelForm):
    when = forms.DateTimeField(widget=AdminSplitDateTime)

    class Meta:
        model = Event
        fields = ('title', 'image', 'venue', 'when', 'description', 'status',)
