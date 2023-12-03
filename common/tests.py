import pytest
from django.urls import reverse_lazy
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_home_template(client):
    """Check template displayed for profiles list."""
    url = reverse_lazy('common:index')
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, 'common/index.html')


@pytest.mark.django_db
def test_admin_access(admin_client):
    """Check connexion to admin with valid admin user."""
    response = admin_client.get('/admin/')
    assert response.status_code == 200
