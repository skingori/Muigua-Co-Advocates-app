# Generated by Django 2.2.2 on 2020-01-19 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lawapp', '0005_auto_20200119_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appearance',
            name='Appearing_lawyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]