import pytest
import requests


@pytest.fixture()
def website_request():
    r = requests.get("http://danielpalacz.pythonanywhere.com/")
    yield r

