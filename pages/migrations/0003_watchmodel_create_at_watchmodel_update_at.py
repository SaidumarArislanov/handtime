# Generated by Django 5.0 on 2023-12-28 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_watch_watchmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchmodel',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='watchmodel',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]