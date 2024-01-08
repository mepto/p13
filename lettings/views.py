import logging

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from lettings.models import Letting

logger = logging.getLogger('main')


def lettings_index(request):
    """Display list of lettings"""
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """Display specific letting."""
    try:
        current_letting = Letting.objects.get(id=letting_id)
    except ObjectDoesNotExist:
        logger.error('Letting for %s does not exist.', letting_id)
        return lettings_index(request)
    context = {
        'title': current_letting.title,
        'address': current_letting.address,
    }
    return render(request, 'lettings/letting.html', context)
