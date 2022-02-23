# Generated by Django 4.0 on 2022-02-22 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='products')),
                ('thumbnail_alt', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]