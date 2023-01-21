from django.shortcuts import render
from django.views import generic
from .models import Event
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