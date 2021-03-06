# Generated by Django 4.0 on 2022-02-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_textimagemodul_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='service')),
                ('thumbnail_alt', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('sort', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='imagemodul',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image_modul'),
        ),
        migrations.AlterField(
            model_name='textimagemodul',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image_text_modul'),
        ),
    ]
