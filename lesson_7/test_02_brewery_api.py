from fake_data import generate_city
import pytest
import requests
from jsonschema import validate
from schemas import brewery_schema


brewery_url = f'https://api.openbrewerydb.org/v1'


@pytest.mark.timer
def test_GET_list_all_breweries_200():
    response = requests.get(
        f"{brewery_url}/breweries")
    ids = [item["id"] for item in response.json()]
    cities = [item["city"] for item in response.json()]
    # Устанавливаем значение переменной brewery_id для pytest
    pytest.brewery_id = ids[0]
    # Устанавливаем значение переменной city для pytest
    pytest.city = cities[0]
    assert response.status_code == 200, 'Wrong status code'
    assert response.json() != [], 'Got empty response'
    assert len(ids) == 50, 'Wrong max number values'
    assert len(cities) == 50, 'Wrong max number values'
    validate(instance=response.json(), schema=brewery_schema)


@pytest.mark.parametrize('id', [1, 'abc'])
def test_GET_brewery_by_id_404(id):
    response_404_error = "Couldn't find Brewery"
    response = requests.get(
        f"{brewery_url}/breweries/{id}")
    assert response.status_code == 404, 'Wrong status code'
    assert response.json() != [], 'Got empty response'
    assert response.json().get("message") == response_404_error, 'Wrong message values'


def test_GET_brewery_by_id_200():
    response = requests.get(
        f"{brewery_url}/breweries/{pytest.brewery_id}")
    assert response.status_code == 200, 'Wrong status code'
    assert response.json() != [], 'Got empty response'
    assert pytest.brewery_id == response.json().get("id"), 'Wrong id'
    validate(instance=response.json(), schema=brewery_schema)


@pytest.mark.parametrize('city', [1, generate_city()])
@pytest.mark.parametrize('page', [1, 'abc'])
def test_GET_brewery_by_city_empty_response_200(city, page):
    data = {
        "by_city": city,
        "per_page": page
    }
    response = requests.get(
        f"{brewery_url}/breweries", params=data)
    assert response.status_code == 200, 'Wrong status code'
    assert response.json() == [], 'Got not empty response'


@pytest.mark.parametrize('page', [1, 2])
def test_GET_brewery_by_city__200(page):
    data = {
        "by_city": pytest.city,
        "per_page": page
    }
    response = requests.get(
        f"{brewery_url}/breweries", params=data)
    cities = [item["city"] for item in response.json()]
    if page == 1:
        assert response.status_code == 200, 'Wrong status code'
        assert response.json() != [], 'Got empty response'
        assert len(cities) == 1, 'Wrong quantity'
        assert cities[0] == pytest.city, 'Wrong city'
        validate(instance=response.json(), schema=brewery_schema)
    if page == 2:
        assert response.status_code == 200, 'Wrong status code'
        assert response.json() != [], 'Got empty response'
        assert len(cities) == 2, 'Wrong quantity'
        assert cities == [pytest.city] * 2, 'Wrong city'
        validate(instance=response.json(), schema=brewery_schema)
