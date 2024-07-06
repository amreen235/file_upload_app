


from django.urls import path
from . import views


urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('upload/', views.display_excel_data, name='main'), 
    path('file/<int:file_id>/', views.file_uploaded, name='file_uploaded'),
    path('report_display/', views.report_display, name='report_display'),
    path('BatchName_display/', views.BatchName_display, name='BatchName_display'),
    path('SubjectName_display/', views.SubjectName_display, name='SubjectName_display'),
    path('get_batch_names/', views.get_batch_names, name='get_batch_names'),
    path('get_subject_names/', views.get_subject_names, name='get_subject_names'),
    path('filter_table', views.filter_table, name='filter_table'),
    
]