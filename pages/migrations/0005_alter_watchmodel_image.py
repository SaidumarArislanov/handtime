# Generated by Django 5.0 on 2023-12-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_watchmodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchmodel',
            name='image',
            field=models.ImageField(upload_to='Watch/'),
        ),
    ]