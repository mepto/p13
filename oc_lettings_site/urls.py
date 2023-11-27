from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='common:index')),
    path('home/', include('common.urls', namespace="common")),
    path('lettings/', include("lettings.urls", namespace="lettings")),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]
