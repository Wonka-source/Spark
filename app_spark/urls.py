from . import views
from django.urls import path


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('create_event', views.create_event, name='create_event'),
    path('user_profile/', views.UserProfile.as_view(), name='user_profile'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),

]
