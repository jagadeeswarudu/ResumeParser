# Generated by Django 5.0.1 on 2024-01-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0005_document_delete_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
