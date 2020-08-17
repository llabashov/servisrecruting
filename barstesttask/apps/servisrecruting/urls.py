from django.urls import path

from . import views

app_name = 'servisrecruting'

urlpatterns = [
    path('', views.startpage, name = 'startpage'),
    path('for_siths', views.for_siths, name = 'for_siths'),
    #path('', views.index_siths, name = 'index_siths'),
    path('<int:sith_id>/', views.detail_siths, name = 'detail_siths'),
    path('<int:sith_id>/recruts_without_shadow_hand', views.recruts_without_shadow_hand, name = 'recruts_without_shadow_hand'),
]