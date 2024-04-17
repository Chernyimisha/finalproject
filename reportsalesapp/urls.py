from django.urls import path
from . import views


urlpatterns = [
     path('index/', views.index, name='index'),
     path('index/crud_report/', views.crud_report, name='crud_report'),
     path('index/crud_detail/', views.crud_detail, name='crud_detail'),
     path('index/crud_report/upload_realization_report_excel/', views.upload_realization_report_excel, name='upload_realization_report_excel'),
     path('index/crud_detail/upload_realization_detail_excel/', views.upload_realization_detail_excel, name='upload_realization_detail_excel'),
     path('index/crud_detail/delete_realization_detail/', views.delete_realization_detail, name='delete_realization_detail'),
     path('index/general_report/', views.general_report, name='general_report'),
     path('index/general_report/upload_general_file_excel/', views.upload_general_file_excel, name='upload_general_file_excel'),
]

