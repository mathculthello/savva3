"""savva3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static



### ROUTER REST
from rest_framework import routers
from calenda.views import EventViewSet

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)




urlpatterns = [
    path(r'api/', include(router.urls)),
    path('base/', include('base.urls')),
    path('allmath/', include('allmath.urls')),
    path('jokes/', include('jokes.urls')),
    path('admin/', admin.site.urls),
    path('calendar/', include('calenda.urls') ),
    path('', include('django.contrib.flatpages.urls')),
    path('', include('pages.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
