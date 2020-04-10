from django.conf.urls import url,include
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^main/$', views.main, name='questionnaire-main'),
    url(r'^questionnaire_save/$', views.questionnaire_save, name='questionnaire-questionnaire_save'),


]