# Generated by Django 3.0.2 on 2020-01-17 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='case_document',
            field=models.FileField(default=1, upload_to='documents'),
            preserve_default=False,
        ),
    ]
