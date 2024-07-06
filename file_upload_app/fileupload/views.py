

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import uploaded_data, uploaded_data_truncated_og
from .forms import FileUploadForm
from django.contrib import messages
import pandas as pd
import sqlite3

def get_batch_names(request):
    report_name = request.GET.get('report_name')
    batch_names = uploaded_data_truncated_og.objects.filter(report_name=report_name).values_list('batch_name', flat=True).distinct()
    return JsonResponse({'batch_names': list(batch_names)})

def get_subject_names(request):
    batch_name = request.GET.get('batch_name')
    subject_names = uploaded_data_truncated_og.objects.filter(batch_name=batch_name).values_list('subject_name', flat=True).distinct()
    return JsonResponse({'subject_names': list(subject_names)})

def load_data(df, sqlite_file_path, table_name, is_ug, report_name):
    column_mapping = {
        'Exam Code': 'exam_code',
        'Student Batch Name': 'student_batch_name',
        'Batch Name': 'batch_name',
        'Class Name': 'class_name',
        'Student Name': 'student_name',
        'RegNo': 'reg_no',
        'Roll No': 'roll_no',
        'Exam Type': 'exam_type',
        'Subject Type': 'subject_type',
        'Subject Code': 'subject_code',
        'Subject Name': 'subject_name',
        'Semester': 'semester',
        'Obt Marks': 'obt_marks',
        'Max Marks': 'max_marks',
        'Obt Grade': 'obt_grade',
        'Is Backlog': 'is_backlog',
        'Is Pass': 'is_pass',
        'Backlog Attempt Number': 'backlog_attempt_number',
        'Credit Point Earned': 'credit_point_earned',
        'Credit Point Offered': 'credit_point_offered',
        'RV Marks': 'rv_marks',
        'RV Updated': 'rv_updated',
    }

    df.rename(columns=column_mapping, inplace=True)
    df['course_category'] = 'UG' if is_ug else 'PG'
    df['report_name'] = report_name

    df['exam_type'] = df['exam_type'].replace({
                    'Formative Assessment (FA)': 'FA',
                    'Summative Assessment (SA)': 'SA'
                    })
    df = df.sort_values(by='roll_no')
    df.loc[(df['exam_type'].isin(['Aggregate', 'SA'])) & (df['obt_marks'] == 0), 'obt_marks'] = ''
    
    truncated_df = df[['exam_code', 'student_batch_name', 'batch_name', 'student_name', 'roll_no', 'exam_type', 
                       'subject_name', 'obt_marks', 'max_marks', 'obt_grade', 'rv_marks', 'rv_updated', 
                       'course_category', 'report_name']]
     
    conn = sqlite3.connect(sqlite_file_path)
    df.to_sql(table_name, conn, if_exists='append', index=False)      
    conn.close()
    
    load_truncated_data(truncated_df, "db.sqlite3", "fileupload_uploaded_data_truncated_og")

def load_truncated_data(truncated_df, sqlite_file_path, table_name):
    
    conn = sqlite3.connect(sqlite_file_path)    
    truncated_df.to_sql(table_name, conn, if_exists = 'append', index=False)
    conn.close()
    
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)

        course_category = request.POST['course_category']
        report_name = request.POST['report_name']

        if form.is_valid():
            # get form values
            course_category = request.POST['course_category']
            report_name = request.POST['report_name']

            uploaded_file = request.FILES['input_excel']
            df = pd.read_excel(uploaded_file)

            # Ensure course_category is either 'UG' or 'PG'
            if course_category.upper() in dict(uploaded_data.COURSE_CATEGORIES):
                is_ug = (course_category == uploaded_data.UG)
            else:
                # Handle invalid case, default to False (PG)
                is_ug = False

            load_data(df, "db.sqlite3", "fileupload_uploaded_data", is_ug, report_name)

            messages.success(request, 'Successfully Uploaded')
            return redirect('main')
    else:
        form = FileUploadForm()
    return render(request, 'fileupload/upload.html', {'form': form})


def display_excel_data(request):
    excel_data = uploaded_data_truncated_og.objects.all()

    reports = uploaded_data_truncated_og.objects.values_list('report_name', flat=True).distinct()
    batch_name = uploaded_data_truncated_og.objects.values_list('batch_name', flat=True).distinct()
    subject_name = uploaded_data_truncated_og.objects.filter(subject_name__isnull = False).values_list('subject_name', flat=True).distinct()
    context = {'excel_data': excel_data, 
               'reports': reports,
               'batch_name' : batch_name,
               'subject_name' : subject_name}
     
    return render(request, 'fileupload/main.html', context)
    

def report_display(request):
    report_dropdown = uploaded_data_truncated_og.objects.values_list('report_name', flat=True).distinct()
    return render(request,'fileupload/main.html', {"report_names_saved" : report_dropdown})

def BatchName_display(request):
    BatchName_dropdown = uploaded_data_truncated_og.objects.values_list('batch_name', flat=True).distinct()
    return render(request,'fileupload/main.html', {"batch_names_saved" : BatchName_dropdown})

def SubjectName_display(request):
    SubjectName_dropdown = uploaded_data_truncated_og.objects.values_list('subject_name', flat=True).distinct()
    # SubjectName_dropdown.delete('None')
    return render(request,'fileupload/main.html', {"subject_names_saved" : SubjectName_dropdown})


def file_uploaded(request, file_id):
    return HttpResponse(f"File uploaded with ID: {file_id}")

def home(request):
    return render(request, 'home.html')


def filtered_data_view(request):
    # Initialize filtered_data to avoid UnboundLocalError
    filtered_data = uploaded_data_truncated_og.objects.none()

    if request.method == "GET":
        report_name = request.GET.get('report_name')
        batch_name = request.GET.get('batch_name')
        subject_name = request.GET.get('subject_name')

        filtered_data = uploaded_data_truncated_og.objects.all()

        if report_name:
            filtered_data = filtered_data.filter(report_name=report_name)
        if batch_name:
            filtered_data = filtered_data.filter(batch_name=batch_name)
        if subject_name:
            filtered_data = filtered_data.filter(subject_name=subject_name)

    context = {
        'filtered_data': filtered_data
    }
    return render(request, 'fileupload/filter.html', context)