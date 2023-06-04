
from logger import log_response
import pytest
import requests

dog_url = f'https://dog.ceo/api'


def test_get_list_all_breeds_200():
    response = requests.get(
        f"{dog_url}/breeds/list/all")
    log_response(response)
    assert response.status_code == 200, 'Wrong status code'
    assert len(response.json()) > 0, 'Got empty response'


def test_get_single_random_image_from_all_dogs_collection_200():
    response = requests.get(
        f"{dog_url}/breeds/image/random")
    log_response(response)
    assert response.status_code == 200, 'Wrong status code'
    assert len(response.json()) > 0, 'Got empty response'
    message = response.json().get('message')
    assert isinstance(message, str), 'Wrong message type'


@pytest.mark.parametrize('random_value', [1, 'abc'])
def test_get_multiple_random_images_from_all_dogs_collection_200(random_value):
    response = requests.get(
        f"{dog_url}/breeds/image/random/{random_value}")
    log_response(response)
    assert response.status_code == 200, 'Wrong status code'
    assert len(response.json()) > 0, 'Got empty response'
    message = response.json().get('message')
    assert isinstance(message, list), 'Wrong message type'


def get_breed_ids():
    response = requests.get(f"{dog_url}/breeds/list/all")
    breed_ids = list(response.json().get("message").keys())[:2]
    return breed_ids


@pytest.mark.parametrize('breed_id', get_breed_ids())
def test_get_multiple_images_by_breed_200(breed_id):
    response = requests.get(f"{dog_url}/breed/{breed_id}/images")
    log_response(response)
    assert response.status_code == 200, 'Wrong status code'
    message = response.json().get('message')
    assert len(message) > 0, 'Got empty message'
    for msg in message:
        assert breed_id in msg, 'Wrong breed_id in message'


@pytest.mark.parametrize('breed_id', [1, 'abc'])
def test_get_multiple_images_by_breed_404(breed_id):
    response_404_message = "Breed not found (master breed does not exist)"
    response = requests.get(f"{dog_url}/breed/{breed_id}/images")
    log_response(response)
    assert response.status_code == 404, 'Wrong status code'
    assert len(response.json()) > 0, 'Got empty response'
    assert response.json().get("message") == response_404_message, 'Wrong message text'