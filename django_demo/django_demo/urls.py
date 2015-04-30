from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from django.conf import settings

from . import hello

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', hello.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
