from django.urls import path
from . import views


urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('upload/', views.display_excel_data, name='main'), 
    path('upload/success/', views.upload_success, name='upload_success'),
    path('file/<int:file_id>/', views.file_uploaded, name='file_uploaded'),
    path('report_display/', views.report_display, name='report_display'),
]