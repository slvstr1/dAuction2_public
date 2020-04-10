from django.conf.urls import url,include

from . import views
from anl import views as views_anl

urlpatterns = [
    #url(r'^graph_data/', views.graph_data),
    #url(r'^myoffers/', views.my_offers),
    #url(r'^standing_transactions/', views.stand_transactions),
    #url(r'^myvouchers/', views.my_vouchers),
    #url(r'^mytrading/', views.my_trading),
    #url(r'^mystats/', views.my_stats),
    # url(r'^mydata/', views.my_data),
    # url(r'^marketdata/', views.market_data),
    url(r'^refresh/', views.refresh),
    url(r'^distrib/', views.distrib),
    url(r'^draw/', views.draw),
    url(r'^cancel_offer/', views.cancel_offer),
    url(r'^player_ready/', views.player_ready),
    url(r'^round_questions/', views.round_questions),
    url(r'^auction_data', views.auction_data),
    url(r'^history_data', views.history_data),
    url(r'^get_timer', views.get_timer),
    # url(r'^analysis_data', views_anl.analysis_data),
]

