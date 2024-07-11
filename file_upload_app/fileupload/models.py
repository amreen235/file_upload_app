
# fileupload/models.py

from django.db import models
    
class uploaded_data(models.Model):
    UG = 'UG'
    PG = 'PG'
    
    COURSE_CATEGORIES = [
        (UG, PG)
    ]

    exam_code = models.CharField(max_length=100, null=True)
    student_batch_name = models.CharField(max_length=255, null=True)
    batch_name = models.CharField(max_length=255, null=True)
    class_name = models.CharField(max_length=255, null=True)
    student_name = models.CharField(max_length=255, null=True)
    reg_no = models.CharField(max_length=50, null=True)
    roll_no = models.CharField(max_length=50, null=True)
    exam_type = models.CharField(max_length=100, null=True)
    subject_type = models.CharField(max_length=100, null=True)
    subject_code = models.CharField(max_length=100, null=True)
    subject_name = models.CharField(max_length=255, null=True)
    semester = models.CharField(max_length=50, null=True)
    obt_marks = models.FloatField(null=True)
    max_marks = models.FloatField(null=True)
    obt_grade = models.CharField(max_length=2, null=True)
    is_backlog = models.CharField(max_length=2, null=True)
    is_pass = models.CharField(max_length=2, null=True)
    backlog_attempt_number = models.IntegerField(null=True)
    credit_point_earned = models.FloatField(null=True)
    credit_point_offered = models.FloatField(null=True)
    rv_marks = models.FloatField(null=True)
    rv_updated = models.CharField(max_length=2, null=True)

    
    course_category = models.CharField(
        max_length=2,
        choices=COURSE_CATEGORIES
    )
    report_name = models.CharField(max_length=255, null=True)

    def str(self):
        return f"{self.report_name} - {self.roll_no} - {self.subject_name}"