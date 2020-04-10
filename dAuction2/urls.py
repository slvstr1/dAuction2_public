
# from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
                # THIS DOESNT WORK
    #url(r'^instructions/', include('instructions.urls', namespace='instructions')),
    # url(r'^forward_and_spot/', include('forward_and_spot.urls', namespace='forward_and_spot')),
    # url(r'^questionnaire/', include('questionnaire.urls', namespace='questionnaire')),
    # url(r'^$', include('instructions.urls', namespace='instructions')),

                       # THIS WORKS - WHY?
    url(r'^instructions/', include('instructions.urls')),
    url(r'^distribution/', include('distribution.urls')),
    url(r'^testing/', include('testing.urls')),
    url(r'^master/', include('master.urls')),
    url(r'^master_earn/', include('master_earn.urls')),
    url(r'^master_data/', include('master_data.urls')),
    url(r'^forward_and_spot/', include('forward_and_spot.urls')),
    url(r'^questionnaire/', include('questionnaire.urls')),
    url(r'^payout/', include('payout.urls')),
    url(r'^$', include('instructions.urls')),

]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
