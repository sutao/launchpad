from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.views.generic import TemplateView

from rest_framework_swagger.views import get_swagger_view
from .api import debug

swagger_schema_view = get_swagger_view(title='Launchpad API')


urlpatterns = [
    url(r'^api/debug/ping/$', debug.Ping.as_view()),

    url(r'^api/auth/', include('rest_auth.urls')),
    url(r'^api/auth/registration/', include('rest_auth.registration.urls')),

]

if settings.DEBUG:
    urlpatterns += [
        url(r'^djangostatic/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
        url(r'^grappelli/', include('grappelli.urls')),
        url(r'^admin/', admin.site.urls),
        url(r'^docs/', swagger_schema_view),
        url(r'^$', TemplateView.as_view(template_name="debug_index.html")),
    ]
else:
    urlpatterns += [
        url(r'^$', TemplateView.as_view(template_name="prod_index.html")),
    ]