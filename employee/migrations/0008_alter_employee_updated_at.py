# Generated by Django 4.0.5 on 2022-09-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_alter_employee_created_at_alter_employee_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='updated_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]