import datetime

import pytest
from django.test import Client
from conf_app.models import ConferenceRoom
from django.contrib.auth.models import User


@pytest.fixture
def client():
    client = Client()
    return client

@pytest.fixture
def client_auth():
    client = Client()
    user = User.objects.create_user(username='zenon',email='zenon@zenon.pl', password='zenon')
    client.force_login(user)
    return client

@pytest.fixture
def manager():
    manager = User.objects.create_user(username='jarek', email='jarek@jarek.pl', password='jarek')
    return manager

@pytest.fixture
def room(manager):
    room = ConferenceRoom.objects.create(manager=manager, name='Tarifa', address='Surfingowa')
    return room

