from django.shortcuts import render

from profiles.models import Profile


def profiles_index(request):
    """Display profiles list."""
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Display specific profile."""
    user_profile = Profile.objects.get(user__username=username)
    context = {'profile': user_profile}
    return render(request, 'profiles/profile.html', context)
