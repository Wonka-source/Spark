from django import forms
from .models import Event
from django.contrib.auth.models import User


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = (
            'title',
            'promotion_company_name',
            'image',
            'where',
            'when',
            'description',
            'status',
        )
