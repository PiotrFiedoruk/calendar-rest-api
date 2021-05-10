from django.contrib import admin
from django.urls import path
from conf_app.views import ConferenceRoomList, ConferenceRoomDetail, EventList, EventDetail, EventCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room-list/', ConferenceRoomList.as_view(), name='room_list'),
    path('room-details/<int:pk>/', ConferenceRoomDetail.as_view(), name='room_detail'),
    path('event-list/', EventList.as_view(), name='event_list'),
    path('event-details/<int:pk>/', EventDetail.as_view(), name='event_detail'),
    path('event-create/', EventCreate.as_view(), name='event_create'),
]
