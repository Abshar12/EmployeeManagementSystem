# Generated by Django 4.0.5 on 2022-09-14 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0020_rename_user_profile_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
