from django.conf.urls import url
from django.views.generic import TemplateView

#from forward_and_spot
from . import views
urlpatterns = [
    url(r'^$', views.main, name='instructions-main'),
    url('page/$', views.page, name='instructions-page'),
]