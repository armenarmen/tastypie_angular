from django.conf.urls import patterns, include, url

from django.contrib import admin
from tastypie.api import Api
from tasty.api.resources import StudentResource, ClassResource, StudentProjectResource

admin.autodiscover()

v1_api = Api(api_name="v1")
v1_api.register(StudentResource())
v1_api.register(ClassResource())
v1_api.register(StudentProjectResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tasty.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'api/doc/',
    include('tastypie_swagger.urls', namespace='tastypie_swagger'),
    kwargs={"tastypie_api_module": "v1_api",
            "namespace": "tastypie_swagger"}
        ),
)
