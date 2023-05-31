import pytest
import requests


dog_url = f'https://dog.ceo/api'


@pytest.mark.timer
def test_GET_list_all_breeds_200():
    response = requests.get(
        f"{dog_url}/breeds/list/all")
    assert response.status_code == 200, 'Wrong status code'
    assert response.json() != [], 'Got empty response'


def test_GET_single_random_image_from_all_dogs_collection_200():
    response = requests.get(
        f"{dog_url}/breeds/image/random")
    assert response.status_code == 200, 'Wrong status code'
    assert response.json() != [], 'Got empty response'


@pytest.mark.parametrize('random_value', [1, 'abc'])
def test_GET_multiple_random_images_from_all_dogs_collection_200(random_value):
    response = requests.get(
        f"{dog_url}/breeds/image/random/{random_value}")
    assert response.status_code == 200, 'Wrong status code'
    assert response.json() != [], 'Got empty response'


def get_breed_ids():
    response = requests.get(f"{dog_url}/breeds/list/all")
    breed_ids = list(response.json().get("message").keys())[:2]
    return breed_ids


@pytest.mark.parametrize('breed_id', get_breed_ids())
def test_GET_multiple_images_by_breed_200(breed_id):
    response = requests.get(f"{dog_url}/breed/{breed_id}/images")
    assert response.status_code == 200, 'Wrong status code'
    assert response.json() != [], 'Got empty response'


@pytest.mark.parametrize('breed_id', [1, 'abc'])
def test_GET_multiple_images_by_breed_404(breed_id):
    response = requests.get(f"{dog_url}/breed/{breed_id}/images")
    assert response.status_code == 404, 'Wrong status code'
    assert response.json() != [], 'Got empty response'
