# Generated by Django 2.2 on 2020-05-06 10:44

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kursus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materi',
            name='isi',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]