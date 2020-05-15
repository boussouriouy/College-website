from django.urls import path
from .import views

#app_name = 'Custom',

urlpatterns = [
    path('tableau', views.table, name='table'),
    
]
