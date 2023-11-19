from django.shortcuts import render


def index(request):
    """Display home page."""
    return render(request, 'common/index.html')
