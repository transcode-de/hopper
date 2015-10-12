from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers

from api.views import FormDataListView, FormDataViewSet

router = routers.DefaultRouter()
router.register(r'v1', FormDataViewSet, base_name='api')

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/$', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^list/$', FormDataListView.as_view(), name='formdata_list'),
    url(r'^api/', include(router.urls)),
    url(r'^forms/', include('form_data.urls')),
    url(r'^', include('landingpage.urls'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
