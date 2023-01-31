from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Event
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from datetime import timedelta


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1, when__gte=(timezone.now() - timedelta(hours=24))).order_by('when')
    template_name = 'index.html'
    paginate_by = 6


class UserProfile(LoginRequiredMixin, View):
    
    def get(self, request):
        user_event_list = Event.objects.filter(promoter=request.user).all().order_by('-created_on')
        today = timezone.now()
        return render(
            request,
            "user_profile.html",
            {
                "user_event_list": user_event_list,
                'page_title': 'Profile',
                'today': today,
            }
        )


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    template = 'event_detail.html'
    context = {        
        'page_title': 'Event Detail',
        'event': event
    }
    if event.status == 1:
        return render(request, template, context)
    elif event.status == 0 and event.promoter == request.user:
        return render(request, template, context)
    else:
        raise PermissionDenied




def about(request):

    return render(
        request,
        "about.html",
)


@login_required(login_url='/accounts/login/')
def create_event(request):

    return render(
        request,
        "create_event.html",
        {"event_form": EventForm()},
    )


