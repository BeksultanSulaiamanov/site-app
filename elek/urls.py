from . import views
from django.urls import path

urlpatterns = [
    path('', views.site, name='site'),
    path('about/', views.about, name='about'),
    path('nout/', views.nout, name='nout'),
    path('chasy/', views.chasy, name='chasy'),
    path('create/', views.create, name='create')
]