# Generated by Django 2.2.2 on 2019-07-10 17:35

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190618_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
