# Generated by Django 5.0.6 on 2024-07-14 15:13

import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingperson',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='avatars'),
        ),
    ]
