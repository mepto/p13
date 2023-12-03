import pytest
from django.urls import reverse_lazy
from pytest_django.asserts import assertTemplateUsed

from lettings.models import Address, Letting


@pytest.fixture
def address():
    """Create fixture for address object."""
    my_address = Address(
        number='42',
        street='fubar street',
        zip_code='34000',
        city='Montpellier',
        state='Occitanie',
        country_iso_code='FRA'
    )
    my_address.save()
    return my_address


@pytest.fixture
def letting(address):
    """Create fixture for letting object."""
    my_letting = Letting(
        address=address,
        title='plouf'
    )
    my_letting.save()
    return my_letting


@pytest.mark.django_db
def test_lettings_list_template(client):
    """Check template displayed for lettings list."""
    url = reverse_lazy('lettings:index')
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/index.html')


@pytest.mark.django_db
def test_lettings_detail_template(client, letting):
    """Check template displayed for a single letting."""
    url = reverse_lazy('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/letting.html')


@pytest.mark.django_db
def test_lettings_detail_data(client, letting):
    """Check address and title of letting possed in context."""
    url = reverse_lazy('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(url)
    title = None
    address = None
    for item in response.context[0]:
        if 'title' in item:
            title = item['title']
        if 'address' in item:
            address = item['address']
    assert title == letting.title
    assert address == letting.address
    assert response.status_code == 200


@pytest.mark.django_db
def test_new_address():
    """Check creation of new address."""
    number = 42
    street = 'magic street'
    city = 'Akila'
    state = 'Neudorf'
    zip_code = 99999
    country_iso_code = 'AKI'
    address = Address.objects.create(
        number=number, street=street, city=city, state=state, zip_code=zip_code,
        country_iso_code=country_iso_code)
    assert address.number == number
    assert address.street == street
    assert address.city == city
    assert address.state == state
    assert address.zip_code == zip_code
    assert address.country_iso_code == country_iso_code


@pytest.mark.django_db
def test_new_letting(address):
    """Chceck creation of new letting."""
    title = 'badaboum'
    letting = Letting.objects.create(
        title=title, address=address)
    assert letting.title == title
    assert letting.address.street == address.street
