# Generated by Django 5.0.6 on 2024-07-14 16:19

import cloudinary_storage.storage
import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_missingperson_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingperson',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='avatars'),
        ),
    ]
