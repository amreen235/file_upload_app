# Generated by Django 5.0.6 on 2024-07-06 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uploaded_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_code', models.CharField(max_length=100, null=True)),
                ('student_batch_name', models.CharField(max_length=255, null=True)),
                ('batch_name', models.CharField(max_length=255, null=True)),
                ('class_name', models.CharField(max_length=255, null=True)),
                ('student_name', models.CharField(max_length=255, null=True)),
                ('reg_no', models.CharField(max_length=50, null=True)),
                ('roll_no', models.CharField(max_length=50, null=True)),
                ('exam_type', models.CharField(max_length=100, null=True)),
                ('subject_type', models.CharField(max_length=100, null=True)),
                ('subject_code', models.CharField(max_length=100, null=True)),
                ('subject_name', models.CharField(max_length=255, null=True)),
                ('semester', models.CharField(max_length=50, null=True)),
                ('obt_marks', models.FloatField(null=True)),
                ('max_marks', models.FloatField(null=True)),
                ('obt_grade', models.CharField(max_length=2, null=True)),
                ('is_backlog', models.CharField(max_length=2, null=True)),
                ('is_pass', models.CharField(max_length=2, null=True)),
                ('backlog_attempt_number', models.IntegerField(null=True)),
                ('credit_point_earned', models.FloatField(null=True)),
                ('credit_point_offered', models.FloatField(null=True)),
                ('rv_marks', models.FloatField(null=True)),
                ('rv_updated', models.CharField(max_length=2, null=True)),
                ('course_category', models.CharField(choices=[('UG', 'PG')], max_length=2)),
                ('report_name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='uploaded_data_truncated_og',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_code', models.CharField(max_length=100, null=True)),
                ('student_batch_name', models.CharField(max_length=255, null=True)),
                ('batch_name', models.CharField(max_length=255, null=True)),
                ('student_name', models.CharField(max_length=255, null=True)),
                ('roll_no', models.CharField(max_length=50, null=True)),
                ('exam_type', models.CharField(max_length=100, null=True)),
                ('subject_name', models.CharField(max_length=255, null=True)),
                ('obt_marks', models.FloatField(null=True)),
                ('max_marks', models.FloatField(null=True)),
                ('obt_grade', models.CharField(max_length=2, null=True)),
                ('is_pass', models.CharField(max_length=2, null=True)),
                ('rv_marks', models.FloatField(null=True)),
                ('rv_updated', models.CharField(max_length=2, null=True)),
                ('course_category', models.CharField(max_length=2, null=True)),
                ('report_name', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
