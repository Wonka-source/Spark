from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Event
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from datetime import timedelta
from django.urls import reverse
from django.contrib import messages


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


@login_required(login_url='/accounts/login/')
def add_event(request):
    
    template = 'create_event.html'

    form = EventForm()

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            event = form.save(commit=False)
            event.promoter = request.user
            event.save()
            messages.success(request, 'Event created successfully.')
            return redirect(
                reverse('user_profile')
            )
        else:
            messages.error(request, 'Something went wrong!, please try again')
            form = EventForm()
    context = {
        'page_title': 'Create Event',
        'form': form
    }


@login_required(login_url='/accounts/login/')
def edit_event(request, event_id):

    event = get_object_or_404(Event, id=event_id)
    if event.promoter != request.user:           
        raise PermissionDenied  

    form = EventForm(instance=event)

    template = 'edit_event.html'

    context = {
        'page_title': 'Edit Event',
        'form': form,
        'event_id': event_id,
    }

    if request.method == 'POST':

        form = EventForm(request.POST, request.FILES, instance=event)

        if form.is_valid():
            form.save()
            messages.success(request, 'Event edited successfully.')
            return redirect(
                reverse('user_profile')
            )

    return render(request, template, context)


@login_required(login_url='/accounts/login/')
def delete_event(request, event_id):

    event = get_object_or_404(Event, id=event_id)
    if event.promoter != request.user:           
        raise PermissionDenied  

    form = EventForm(instance=event)

    template = 'delete_event.html'

    context = {
        'page_title': 'Delete Event',
        'form': form,
        'event_id': event_id,
    }

    if request.method == 'POST':

        form = EventForm(request.POST, request.FILES, instance=event)

        if form.is_valid():
            event.delete()
            messages.error(request, 'Event deleted.')
            return redirect(
                reverse('user_profile')
            )

    return render(request, template, context)


def about(request):
    context = {                
        'page_title': 'About',
    }
    return render(
        request,
        "about.html",
        context
    )


def handler404(request, exception):
    
    return render(request, "404.html", status=404)


def handler500(request):

    return render(request, "500.html", status=500)


def handler403(request, exception):

    return render(request, "403.html", status=403)


def handler405(request, exception):

    return render(request, "405.html", status=405)
