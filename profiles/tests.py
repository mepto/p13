import pytest
from django.urls import reverse_lazy
from pytest_django.asserts import assertTemplateUsed

from profiles.models import Profile, User


@pytest.fixture
def user():
    """Create fixture for user."""
    my_user = User(
        username='smorgan',
        first_name='sarah',
        last_name='morgan',
        email='sarah.morgan@constellation.io'
    )
    my_user.save()
    return my_user


@pytest.fixture
def profile(user):
    """Create fixture for profile."""
    my_profile = Profile(
        user=user,
        favorite_city='New Atlantis'
    )
    my_profile.save()
    return my_profile


@pytest.mark.django_db
def test_profiles_list_template(client):
    """Check template displayed for profiles list."""
    url = reverse_lazy('profiles:index')
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/index.html')


@pytest.mark.django_db
def test_profiles_detail_template(client, profile):
    """Check template displayed for a single profile."""
    url = reverse_lazy('profiles:profile', kwargs={'username': profile.user.username})
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/profile.html')


@pytest.mark.django_db
def test_profiles_detail_data(client, profile):
    """Check address and title of profile possed in context."""
    url = reverse_lazy('profiles:profile', kwargs={'username': profile.user.username})
    response = client.get(url)
    user_profile = None
    for item in response.context[0]:
        if 'profile' in item:
            user_profile = item['profile']
    assert user_profile == profile
    assert response.status_code == 200


@pytest.mark.django_db
def test_new_user(django_user_model):
    """Check creation of new user."""
    name = 'SamCoe'
    user = django_user_model.objects.create(
        username=name, first_name='sam', last_name='coe',
        password='something', email='sam.coe@constellation.io')
    assert user.username == name


@pytest.mark.django_db
def test_new_profile(user):
    """Check creation of new profile."""
    favorite_city = 'Neon'
    profile = Profile.objects.create(user=user, favorite_city=favorite_city)
    assert profile.user.username == 'smorgan'
    assert profile.favorite_city == favorite_city
