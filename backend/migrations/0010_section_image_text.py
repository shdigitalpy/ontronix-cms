# Generated by Django 4.0 on 2022-02-23 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_textimagemodul'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='image_text',
            field=models.ManyToManyField(blank=True, related_name='section_text_image', to='backend.TextImageModul'),
        ),
    ]