from django.shortcuts import get_object_or_404, render

from lettings.models import Letting


def lettings_index(request):
    """Display list of lettings"""
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """Display specific letting."""
    current_letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': current_letting.title,
        'address': current_letting.address,
    }
    return render(request, 'lettings/letting.html', context)
