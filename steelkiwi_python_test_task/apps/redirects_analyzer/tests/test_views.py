import pytest
from django.urls import reverse
from mixer.backend.django import mixer

from redirects_analyzer.models import RedirectData
from redirects_analyzer.views import RedirectDataViewSet


pytestmark = pytest.mark.django_db


@pytest.mark.urls('redirects_analyzer.urls')
def test_list(api_client):
    url = reverse('redirect-list')
    mixer.cycle(20).blend(RedirectData)
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data.get('count') == 20


@pytest.mark.urls('redirects_analyzer.urls')
def test_create(api_client):
    url = reverse('redirect-list')
    data = {
        'redirect_url': "https://steelkiwi.com/jobs/",
    }
    response = api_client.post(url, data=data)
    assert response.status_code == 302


@pytest.mark.urls('redirects_analyzer.urls')
def test_top(api_client):
    url = reverse('redirect-top')
    mixer.cycle(10).blend(RedirectData)
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data.get('count') == 10


@pytest.mark.urls('redirects_analyzer.urls')
def test_by_domain(api_client):
    url = reverse('redirect-by-domain')
    response = api_client.get(url)
    assert response.status_code == 200
