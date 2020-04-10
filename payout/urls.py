from django.conf.urls import url,include
from django.views.generic import TemplateView

from payout import views


urlpatterns = [
    url(r'^main/$', views.main, name='payout-main'),

]