# Generated by Django 5.0.1 on 2024-01-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0006_alter_document_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='certification_name',
            field=models.CharField(default='Not available', max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='company',
            field=models.CharField(default='Not available', max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='current_profession',
            field=models.CharField(default='Not available', max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='degree',
            field=models.CharField(default='Not available', max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='email',
            field=models.EmailField(default='Not available', max_length=254),
        ),
        migrations.AddField(
            model_name='document',
            name='establishment',
            field=models.CharField(default='Not available', max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='interest',
            field=models.CharField(default='Not available', max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='language_name',
            field=models.CharField(default='Not available', max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='location',
            field=models.CharField(default='Not available', max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(default='Not available', max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='phone',
            field=models.CharField(default='Not available', max_length=20),
        ),
        migrations.AddField(
            model_name='document',
            name='skill_name',
            field=models.CharField(default='Not available', max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='work_title',
            field=models.CharField(default='Not available', max_length=255),
        ),
    ]
