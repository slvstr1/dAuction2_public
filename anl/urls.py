from django.conf.urls import url,include

from . import views

urlpatterns = [
    url(r'^market/', views.market),
    url(r'^results/', views.results),
    url(r'^analysis_data', views.analysis_data),
]

