# Generated by Django 5.0.1 on 2024-01-26 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0007_document_certification_name_document_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='degree',
        ),
        migrations.AddField(
            model_name='document',
            name='education_details',
            field=models.CharField(default='Not available', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='certification_name',
            field=models.CharField(default='Not available', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='company',
            field=models.CharField(default='Not available', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='current_profession',
            field=models.CharField(default='Not available', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='email',
            field=models.EmailField(default='Not available', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='establishment',
            field=models.CharField(default='Not available', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='interest',
            field=models.CharField(default='Not available', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='language_name',
            field=models.CharField(default='Not available', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='location',
            field=models.CharField(default='Not available', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(default='Not available', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='phone',
            field=models.CharField(default='Not available', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='skill_name',
            field=models.CharField(default='Not available', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='work_title',
            field=models.CharField(default='Not available', max_length=255, null=True),
        ),
    ]
