import pytest
import requests
from logger import log_response

jsonplaceholder_url = f'https://jsonplaceholder.typicode.com'


def test_get_list_all_posts_200():
    response = requests.get(
        f"{jsonplaceholder_url}/posts")
    log_response(response)
    ids = [item["id"] for item in response.json()]
    assert response.status_code == 200, 'Wrong status code'
    assert len(response.json()) > 0, 'Got empty response'
    assert len(ids) == 100, 'Wrong max number values'


@pytest.fixture(scope="module")
def post_id_fixture():
    response = requests.get(f"{jsonplaceholder_url}/posts")
    ids = [item["id"] for item in response.json()]
    brewery_id = ids[0]
    return brewery_id


def test_get_post_by_id_200(post_id_fixture):
    post_id = post_id_fixture
    response = requests.get(
        f"{jsonplaceholder_url}/posts/{post_id}")
    log_response(response)
    assert response.status_code == 200, 'Wrong status code'
    assert len(response.json()) > 0, 'Got empty response'
    assert post_id == response.json().get("id"), 'Wrong post_id'


@pytest.mark.parametrize(
    'title, body, user_id',
    [
        (1, 1, 1),
        ('abc', 'abc', 'abc')
    ]
)
def test_POST_create_post_201(title, body, user_id):
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(
        f"{jsonplaceholder_url}/posts", data=data)
    log_response(response)
    assert response.status_code == 201, 'Wrong status code'
    assert len(response.json()) > 0, 'Got empty response'


@pytest.mark.parametrize('id', [2, 'def'])
@pytest.mark.parametrize('title', [2, 'def'])
@pytest.mark.parametrize('body', [2, 'def'])
@pytest.mark.parametrize('user_id', [2, 'def'])
def test_put_update_post_200(id, title, body, user_id):
    data = {
        "id": id,
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.put(
        f"{jsonplaceholder_url}/posts/1", data=data)
    log_response(response)
    assert response.status_code == 200, 'Wrong status code'
    assert len(response.json()) > 0, 'Got empty response'


@pytest.mark.parametrize('title', [3, 'ghi'])
def test_patch_update_post_200(title):
    data = {
        "title": title
    }
    response = requests.patch(
        f"{jsonplaceholder_url}/posts/1", data=data)
    log_response(response)
    assert response.status_code == 200, 'Wrong status code'
    assert len(response.json()) > 0, 'Got empty response'


def test_delete_delete_post_200():
    response = requests.delete(
        f"{jsonplaceholder_url}/posts/1")
    log_response(response)
    assert response.status_code == 200, 'Wrong status code'
