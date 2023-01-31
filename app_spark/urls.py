from . import views
from django.urls import path


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('create_event', views.add_event, name='create_event'),
    path('user_profile/', views.UserProfile.as_view(), name='user_profile'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
]

handler404 = 'app_spark.views.handler404'
handler500 = 'app_spark.views.handler500'
handler403 = 'app_spark.views.handler403'
handler405 = 'app_spark.views.handler405'
