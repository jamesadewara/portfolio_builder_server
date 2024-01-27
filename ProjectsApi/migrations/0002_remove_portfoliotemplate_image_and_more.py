# Generated by Django 5.0.1 on 2024-01-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoliotemplate',
            name='image',
        ),
        migrations.AddField(
            model_name='portfoliotemplate',
            name='default_image',
            field=models.ImageField(default='', upload_to='thumbnail/img/templates/default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfoliotemplate',
            name='mobile_image',
            field=models.ImageField(default='', upload_to='thumbnail/img/templates/mobile'),
            preserve_default=False,
        ),
    ]
