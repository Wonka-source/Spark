from django.shortcuts import render
from django.views import generic
from .models import Event
from django.contrib.auth.decorators import login_required
from .forms import EventForm
# from django.shortcuts import redirect
# from allauth.account.views import SignupView


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-when')
    template_name = 'index.html'
    paginate_by = 6


# class SignupView(allauth.account.views.SignupView):

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         return redirect('home')

def about(request):

    return render(
        request,
        "about.html",
)


@login_required(login_url='/accounts/login/')
def view_profile(request):
    context = {
        'user': request.user

    }
    return render(request, 'profile.html', context)


@login_required(login_url='/accounts/login/')
def create_event(request):

    return render(
        request,
        "create_event.html",
        {"event_form": EventForm()},
    )


# @admin.register(Event)

# @login_required(login_url='/accounts/login/')
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
