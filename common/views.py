from django.shortcuts import render


def index(request):
    """Display home page."""
    return render(request, 'common/index.html')


def error_404(request, exception=None):
    context = {'exception': exception}
    return render(request, 'common/404.html', context)


def error_500(request, exception=None):
    if exception:
        context = {'exception': exception}
    return render(request, 'common/500.html', context)
