# Generated by Django 4.0.5 on 2022-09-12 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0016_alter_employee_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
