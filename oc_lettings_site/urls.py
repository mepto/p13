from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', include('common.urls', namespace="common")),
    path('home/', include('common.urls', namespace="common")),
    path('lettings/', include("lettings.urls", namespace="lettings")),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]
