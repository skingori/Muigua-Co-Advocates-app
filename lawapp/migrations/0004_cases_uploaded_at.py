# Generated by Django 3.0.2 on 2020-01-17 08:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lawapp', '0003_auto_20200117_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
