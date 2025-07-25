from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('stock-data/', views.get_stock_data, name='stock-data'),
    re_path(r'^candles/(?P<symbol>[^/]+)/$', views.get_candles, name='candles'),
]
