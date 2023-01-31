from django.shortcuts import render
from django.views import generic
from .models import Event
from django.contrib.auth.decorators import login_required
from .forms import EventForm


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-when')
    template_name = 'index.html'
    paginate_by = 6


def about(request):

    return render(
        request,
        "about.html",
)


# @login_required(login_url='/accounts/login/')
# def view_profile(request):
#     context = {
#         'user': request.user

#     }
#     return render(request, 'profile.html', context)


@login_required(login_url='/accounts/login/')
def create_event(request):

    return render(
        request,
        "create_event.html",
        {"event_form": EventForm()},
    )


