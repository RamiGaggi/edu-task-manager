# Generated by Django 3.2.5 on 2021-07-18 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='assignee_id',
            new_name='assignee',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='status_id',
            new_name='status',
        ),
    ]
