import logging

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render

from profiles.models import Profile


logger = logging.getLogger('main')


def profiles_index(request):
    """Display profiles list."""
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Display specific profile."""
    try:
        user_profile = Profile.objects.get(user__username=username)
        context = {'profile': user_profile}
    except ObjectDoesNotExist:
        logger.error(f'Profile for {username} does not exist.')
        return profiles_index(request)
    return render(request, 'profiles/profile.html', context)
