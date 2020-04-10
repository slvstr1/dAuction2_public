from __future__ import absolute_import, unicode_literals

try:
    from django.conf.urls import (include, url,handler500, handler404)
except ImportError:
    from django.conf.urls.defaults import (include, url,  handler500, handler404)
from django.contrib import admin

admin.autodiscover()
from django.conf.urls import url
from master import views, master_api
from master_earn import views as views_earn

urlpatterns = [
    url('', views_earn.main_earnings, name='views_earnings'),
    url(r'^login', views.login_user,name='master-login_user'),
    url(r'^logout', views.logout),
    url(r'^ajax_admin', master_api.ajax_admin),
    url('master_screen_select/$', views.master_screen_select, name='master_screen_select'),



]
# from django.contrib import admin
# from django.conf.urls import include, url

from django.conf import settings
from django.conf.urls import include, url

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]