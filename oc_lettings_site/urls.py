from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='common:index')),
    path('home/', include('common.urls', namespace="common")),
    path('lettings/', include("lettings.urls", namespace="lettings")),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]

handler404 = 'common.views.error_404'
handler500 = 'common.views.error_500'
