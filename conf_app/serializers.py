import datetime
from rest_framework import serializers, permissions
from conf_app.models import Profile, ConferenceRoom, CalendarEvent


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email')
        permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class ConferenceRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConferenceRoom
        fields = ('name', 'manager', 'address', 'events')


class CalendarEventSerializer(serializers.ModelSerializer):
    location = ConferenceRoomSerializer(read_only=True)

    class Meta:
        model = CalendarEvent
        fields = ('owner', 'event_name', 'meeting_agenda', 'start', 'end', 'participants', 'location')


class CalendarCreateEventSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # some POST validation
    def validate(self, data):
        time_diff = (data['end'] - data['start']).total_seconds()
        if time_diff / 60 > 480:
            raise serializers.ValidationError('Meeting cannot last longer than 8 hours')
        time_now = datetime.datetime.now(datetime.timezone.utc)
        if data['start'] < time_now:
            raise serializers.ValidationError('Meeting cannot start in the past')
        if data['end'] < data['start']:
            raise serializers.ValidationError('Meeting end date cannot be before start date')
        return data

    class Meta:
        model = CalendarEvent
        fields = '__all__'
