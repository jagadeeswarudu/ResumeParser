# Generated by Django 5.0.1 on 2024-02-01 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0011_alter_document_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
