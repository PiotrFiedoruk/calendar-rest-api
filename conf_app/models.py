from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Profile(User):
    company_id = models.CharField(max_length=64, null=True)


class ConferenceRoom(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager')
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return f'name: {self.name}\n manager: {self.manager.first_name}\n address: {self.address}'

class CalendarEvent(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    location = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE, related_name='events')
    event_name = models.CharField(max_length=64)
    meeting_agenda = models.TextField(max_length=2400)
    start = models.DateTimeField()
    end = models.DateTimeField()
    participants = models.CharField(max_length=1024)

    def __str__(self):
        return self.event_name




