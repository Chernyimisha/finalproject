from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='index'),
     path('crud_report/', views.crud_report, name='crud_report'),
     path('crud_detail/', views.crud_detail, name='crud_detail'),
     path('crud_report/upload_realization_report_excel/', views.upload_realization_report_excel, name='upload_realization_report_excel'),
     path('crud_detail/upload_realization_detail_excel/', views.upload_realization_detail_excel, name='upload_realization_detail_excel'),
     path('crud_detail/delete_realization_detail/', views.delete_realization_detail, name='delete_realization_detail'),
     path('general_report/', views.general_report, name='general_report'),
     path('general_report/upload_general_file_excel/', views.upload_general_file_excel, name='upload_general_file_excel'),
]

