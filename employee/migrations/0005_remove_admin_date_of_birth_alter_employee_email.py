# Generated by Django 4.0.5 on 2022-08-30 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_delete_ranjeet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]