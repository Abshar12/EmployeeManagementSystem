# Generated by Django 4.0.5 on 2022-09-12 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_employee_resume_alter_employee_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='resume',
            field=models.FileField(upload_to='employee/resume'),
        ),
    ]
