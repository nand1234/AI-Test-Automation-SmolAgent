import requests
import pytest

def test_successful_get_request():
    url = "https://httpbin.org/get"
    response = requests.get(url.strip())
    assert response.status_code == 200
    assert response.json().get('args') == {}

def test_extra_spaces_in_url():
    url = "   https://httpbin. org/  get   "
    response = requests.get(url.strip())
    assert response.status_code == 200
    assert response.json().get('args') == {}

def test_get_request_with_trailing_slash():
    url = "https://httpbin.org/get/"
    response = requests.get(url.strip())
    assert response.status_code == 200
    assert response.json().get('args') == {}

def test_get_request_with_unexpected_http_method():
    url = "https://httpbin.org/get"
    response = requests.post(url)
    assert response.status_code == 405
    assert 'error' in response.json()

def test_get_request_with_invalid_url():
    url = "https://invalid-url/get"
    try:
        response = requests.get(url)
    except requests.RequestException as e:
        assert True
        return
    assert response.status_code != 200
    assert 'error' in response.json()
