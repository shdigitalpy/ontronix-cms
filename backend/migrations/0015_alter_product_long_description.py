# Generated by Django 4.0 on 2022-02-25 09:41

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_product_long_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='long_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]