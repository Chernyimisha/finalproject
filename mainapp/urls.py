from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='index'),
     path('api/', views.settings_api, name='settings_api'),
     path('api/settings_api/', views.input_api_key, name='input_api_key'),
     path('api/settings_url/', views.input_api_url, name='input_api_url'),

]

