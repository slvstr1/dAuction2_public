from django.conf.urls import url,include
from django.views.generic import TemplateView

from forward_and_spot import views

urlpatterns = [
    url(r'^main/$', views.main, name='forward_and_spot-main'),
    url(r'^forward_and_spot/set_offer/', views.set_offer, name='forward_and_spot-set_offer'),
]