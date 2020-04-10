from django.conf.urls import url,include
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    # url(r'^login', views.login_user,name='distribution-login'),
    # url(r'^logout', views.logout_user,name='distribution-logout'),
    url(r'^$', views.main, name='distribution-main'),
    # url(r'draw', views.draw, name='distribution-draw'),
    # url(r'next', views.next, name='distribution-next'),
    # url(r'contin', views.contin, name='distribution-contin'),

]