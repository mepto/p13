from django.shortcuts import render

from profiles.models import Profile


def profiles_index(request):
    """Display profiles list."""
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)


def profile(request, username):
    """Display specific profile."""
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)
