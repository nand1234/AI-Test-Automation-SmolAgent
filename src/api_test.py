
import requests

def test_successful_get_request_without_query_params():
    url = "https://httpbin.org/get"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["args"] == {}

def test_extra_spaces_in_url():
    url = "   https://httpbin. org/  get   "
    response = requests.get(url.strip())
    assert response.status_code == 200
    assert response.json()["args"] == {}

def test_get_request_with_trailing_slash():
    url = "https://httpbin.org/get/"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["args"] == {}

def test_get_request_with_unexpected_http_method():
    url = "https://httpbin.org/get"
    response = requests.post(url)
    assert response.status_code == 405
    assert "error" in response.json()

def test_get_request_with_invalid_url():
    url = "https://invalid-url/get"
    try:
        response = requests.get(url)
        assert response.status_code != 200
        assert "error" in response.text
    except requests.exceptions.RequestException:
        assert True, "An exception was raised, likely due to an invalid URL"
