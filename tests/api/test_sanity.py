import requests


def test_website_availability(website_request):
    assert website_request.status_code == 200
