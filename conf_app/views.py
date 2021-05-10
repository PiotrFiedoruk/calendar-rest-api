from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from conf_app.models import ConferenceRoom, CalendarEvent, Profile
from rest_framework import generics
from conf_app.serializers import ConferenceRoomSerializer, UserSerializer, CalendarEventSerializer, \
    CalendarCreateEventSerializer

class IsParticipatingOrRoomManager(BasePermission):
    """Custom viewpoint permission: only participant or room manager can view event"""
    def has_object_permission(self, request, view, obj):

        current_user_email = request.user.email
        room_manager_email = obj.location.manager.email
        participant_list = ''.join(obj.participants)
        if current_user_email == room_manager_email:
            return True
        elif current_user_email in participant_list:
            return True
        return False

# class generic views
class UserList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

class ConferenceRoomList(generics.ListCreateAPIView):
    """/room-list/"""
    queryset = ConferenceRoom.objects.all()
    serializer_class = ConferenceRoomSerializer
    permission_classes = (IsAuthenticated,)


class ConferenceRoomDetail(generics.RetrieveUpdateDestroyAPIView):
    """/room-details/id/"""
    queryset = ConferenceRoom.objects.all()
    serializer_class = ConferenceRoomSerializer
    permission_classes = (IsAuthenticated,)


class EventList(generics.ListAPIView):
    """/event-list/  -   additional filters added"""
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['event_name', 'meeting_agenda', 'location', 'start']

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """/event-details/id/"""
    permission_classes = (IsAuthenticated, IsParticipatingOrRoomManager, )
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventSerializer


class EventCreate(generics.CreateAPIView):
    """/event-create/"""
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarCreateEventSerializer
    permission_classes = (IsAuthenticated,)



