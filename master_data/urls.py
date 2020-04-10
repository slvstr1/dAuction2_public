from __future__ import absolute_import, unicode_literals
try:
    from django.conf.urls import (include, url, handler500, handler404)
except ImportError:
    from django.conf.urls.defaults import (include, url, handler500, handler404)
from django.contrib import admin
admin.autodiscover()

from django.conf.urls import url
from master import views, master_api
from master_data import views as views_data
from master_earn import views as views_earn

urlpatterns = [
    url(r'', views_earn.payment_data_handle, name='master_payment_data_handle'),
    url(r'^login', views.login_user,name='master-login_user'),
    url(r'^logout', views.logout),
    url(r'^ajax_admin', master_api.ajax_admin),
    ##### urls for user login/logout

    #####
    url('set_state/$', views.set_state, name='master-set_state'),
    url('set_state/$', views.set_state, name='master-set_state2'),
    url('subject_select/$', views_data.subject_select, name='master-subject_select'),
    url('$', views_data.main2, name='master_data_main'),
    url('data_handler/$', views_data.data_handler, name='master_data_handler'),
    url('master_screen_select/$', views.master_screen_select, name='master_screen_select'),
    url('parameters_set/$', views.parameters_set, name='master-parameters_set'),
    url('data_handler/$', views_data.data_handler, name='master_data_handler'),


]
from django.contrib import admin
from django.conf.urls import include, url

from django.conf import settings
from django.conf.urls import include, url

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]