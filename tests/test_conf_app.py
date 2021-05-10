import pytest

# testing room endpoints responses
def test_room_list_non_auth(client):
    response = client.get('/room-list/')
    assert response.status_code == 403

@pytest.mark.django_db
def test_room_list_code_auth(client_auth, room):
    response = client_auth.get('/room-list/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_room_list_content_auth(client_auth, room):
    response = client_auth.get('/room-list/')
    assert len(response.json()) == 1

@pytest.mark.django_db
def test_room_list_post_auth(client_auth, room):
    manager = room.manager
    name = room.name
    address = room.address
    response = client_auth.post('/room-list/', {'manager': str(manager.id), 'name': str(name), 'address': str(address)})
    assert response.status_code == 201

@pytest.mark.django_db
def test_room_detail_code_auth(client_auth, room):
    response = client_auth.get(f'/room-details/{room.id}/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_room_detail_content_auth(client_auth, room):
    response = client_auth.get(f'/room-details/{room.id}/')
    assert response.json()['name'] == 'Tarifa'
