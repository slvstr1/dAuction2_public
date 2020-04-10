# from django.conf.urls import include, url
from master.views import custom_error_view
# from django.conf import settings
# from django.views.static import serve
# import os




from django.conf import settings
from django.conf.urls import include, url
from functools import partial


urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^master/', include('master.urls')),
    url(r'^master_data/', include('master_data.urls')),
    url(r'^instructions/', include('instructions.urls')),
    url(r'^distribution/', include('distribution.urls')),
    url(r'^testing/', include('testing.urls')),
    url(r'^forward_and_spot/', include('forward_and_spot.urls')),
    url(r'^questionnaire/', include('questionnaire.urls')),
    url(r'^payout/', include('payout.urls')),
    url(r'^', include('master.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^anl/', include('anl.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

# custom error pages with refresh url
if not settings.DEBUG:
    handler400 = partial(custom_error_view, error_code=400)
    handler403 = partial(custom_error_view, error_code=403)
    handler404 = partial(custom_error_view, error_code=404)
    handler500 = partial(custom_error_view, error_code=500)