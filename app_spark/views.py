from django.shortcuts import render
from django.views import generic, View
from .models import Event
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-when')
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


