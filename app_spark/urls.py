from . import views
from django.urls import path


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.view_profile, name='profile'),
    path('create_event', views.create_event, name='create_event'),
]
