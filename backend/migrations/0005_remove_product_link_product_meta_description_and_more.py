# Generated by Django 4.0 on 2022-02-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='link',
        ),
        migrations.AddField(
            model_name='product',
            name='meta_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sort',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
