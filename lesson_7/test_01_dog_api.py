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


@pytest.mark.parametrize('random_value', [-1, 0, 'abc', 50, 51])
def test_GET_multiple_random_images_from_all_dogs_collection_200(random_value):
    response = requests.get(
        f"{dog_url}/breeds/image/random/{random_value}")
    if random_value == -1:
        assert response.status_code == 200, 'Wrong status code'
        assert response.json() != [], 'Got empty response'
        assert len(response.json().get("message")) == 1, 'Wrong message values'
    elif random_value == 0:
        assert response.status_code == 200, 'Wrong status code'
        assert response.json() != [], 'Got empty response'
        assert len(response.json().get("message")) == 1, 'Wrong message values'
    elif random_value == 'abc':
        assert response.status_code == 200, 'Wrong status code'
        assert response.json() != [], 'Got empty response'
        assert len(response.json().get("message")) == 1, 'Wrong message values'
    elif random_value == 50:
        assert response.status_code == 200, 'Wrong status code'
        assert response.json() != [], 'Got empty response'
        assert len(response.json().get("message")
                   ) == 50, 'Wrong message values'
    elif random_value == 51:
        assert response.status_code == 200, 'Wrong status code'
        assert response.json() != [], 'Got empty response'
        assert len(response.json().get("message")
                   ) == 50, 'Wrong message values'


@pytest.mark.parametrize('breed', [0, 'abc', "affenpinscher"])
def test_GET_multiple_images_by_breed_200_404(breed):
    response_404_error = "Breed not found (master breed does not exist)"
    response = requests.get(
        f"{dog_url}/breed/{breed}/images")
    if breed == 0:
        assert response.status_code == 404, 'Wrong status code'
        assert response.json() != [], 'Got empty response'
        assert response.json().get("message") == response_404_error, 'Wrong message values'
    elif breed == 'abc':
        assert response.status_code == 404, 'Wrong status code'
        assert response.json() != [], 'Got empty response'
        assert response.json().get("message") == response_404_error, 'Wrong message values'
    elif breed == 'affenpinscher':
        assert response.status_code == 200, 'Wrong status code'
        assert response.json() != [], 'Got empty response'


@pytest.mark.parametrize('breed', [0, 'abc', "affenpinscher"])
def test_GET_single_random_image_by_breed_200_404(breed):
    response_404_error = "Breed not found (master breed does not exist)"
    response = requests.get(
        f"{dog_url}/breed/{breed}/images/random")
    if breed == 0:
        assert response.status_code == 404, 'Wrong status code'
        assert response.json() != [], 'Got empty response'
        assert response.json().get("message") == response_404_error, 'Wrong message values'
    elif breed == 'abc':
        assert response.status_code == 404, 'Wrong status code'
        assert response.json() != [], 'Got empty response'
        assert response.json().get("message") == response_404_error, 'Wrong message values'
    elif breed == 'affenpinscher':
        assert response.status_code == 200, 'Wrong status code'
        assert response.json() != [], 'Got empty response'
