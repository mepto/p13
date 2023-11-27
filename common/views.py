# import logging

from django.shortcuts import render

# logger = logging.getLogger('django')


def index(request):
    """Display home page."""
    return render(request, 'common/index.html')


# def error_404(request, exception=None):
def error_404(request, exception=None):
    """Display custom error 404 page."""
    # logger.error(exception)
    print(exception)
    return render(request, 'common/404.html')


def error_500(request, exception=None):
    """Display custom error 500 page."""
    # logger.error(exception)
    print(exception)
    return render(request, 'common/500.html')
