# Generated by Django 4.0.5 on 2022-09-16 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0022_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='updated_at',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
