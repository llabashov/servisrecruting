from django.urls import path

from . import views
from .views import *

app_name = 'servisrecruting'

urlpatterns = [
    path('', views.startpage, name = 'startpage'),
    path('for_siths', views.for_siths, name = 'for_siths'),
    #path('', views.index_siths, name = 'index_siths'),
    path('recrut/create_recrut', RecrutCreate.as_view(), name = 'recrut_create_url'),
    path('<int:sith_id>/', views.detail_siths, name = 'detail_siths'),
    path('<int:sith_id>/recruts_without_shadow_hand', views.recruts_without_shadow_hand, name = 'recruts_without_shadow_hand'),
]