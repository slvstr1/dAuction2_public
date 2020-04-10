from __future__ import absolute_import, unicode_literals

try:
    from django.conf.urls import (include, url,
                                  handler500, handler404)
except ImportError:
    from django.conf.urls.defaults import (include, url,  # noqa
                                  handler500, handler404)
from django.contrib import admin
admin.autodiscover()


from django.conf.urls import url

from master_sanl import views as views_sanl
from master_data import views as views_data
from master_earn import views as views_earn
from master import views, master_api
# from master import functions

urlpatterns = [
    # changed to use views
    url(r'^login', views.login_user,name='master-login_user'),
    url(r'^logout', views.logout_user),
    url(r'^$', views.main, name='master-main'),
    # url for admin ajax
    url(r'^ajax_admin', master_api.ajax_admin),
    ##### urls for user login/logout
    url(r'^master_earnings', views_earn.main_earnings, name='master_earnings'),
    url('set_state/$', views.set_state, name='master-set_state'),
    url('set_state/$', views.set_state, name='master-set_state2'),
    url('master_sanl_handler/$', views_sanl.master_sanl_handler, name='master_sanl_handler'),
    url('admin/', admin.site.urls),
    url('subject_select/$', views.subject_select, name='master-subject_select'),
    url('master_sanl/$', views_sanl.main_sanl, name='master_sanl'),
    url('master_data_main/$', views_data.main2, name='master_data_main'),
    url('data_handler/$', views_data.data_handler, name='master_data_handler'),
    url(r'^master_earn_assistant_info/', views_earn.master_earn_assistant_info, name='master_earn_assistant_info'),
    url('master_screen_select/$', views.master_screen_select, name='master_screen_select'),
    url('parameters_set/$', views.parameters_set, name='master-parameters_set'),


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