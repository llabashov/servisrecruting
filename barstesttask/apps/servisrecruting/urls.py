from django.urls import path

from . import views
from .views import *

app_name = 'servisrecruting'

urlpatterns = [
    path('', views.startpage, name = 'startpage'),
    #path('', views.index_siths, name = 'index_siths'),
    path('recrut/recrut_create', RecrutCreate.as_view(), name = 'recrut_create_url'),
    path('siths/for_siths', views.for_siths, name = 'for_siths'),
    path('siths/<str:sith_name>/', views.detail_siths, name = 'detail_siths'),
    path('siths/<str:sith_name>/recruts_without_shadow_hand', views.recruts_without_shadow_hand, name = 'recruts_without_shadow_hand'),
]