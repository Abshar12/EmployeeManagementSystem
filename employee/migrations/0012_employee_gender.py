# Generated by Django 4.0.5 on 2022-09-10 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_remove_employee_gender_alter_admin_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.gender'),
        ),
    ]