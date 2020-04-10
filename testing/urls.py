from django.conf.urls import url,include
from django.views.generic import TemplateView

from testing import views


urlpatterns = [
    url(r'^main/', views.main, name='testing-main'),
    url(r'', views.main, name='testing-main'),
]