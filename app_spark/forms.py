from django import forms
from .models import Event
from django.contrib.auth.models import User


class EventForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Include a venue address here...'}))

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
