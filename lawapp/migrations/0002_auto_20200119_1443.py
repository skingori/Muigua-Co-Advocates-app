# Generated by Django 2.2.2 on 2020-01-19 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lawapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representation',
            name='Represented_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lawapp.Clients'),
        ),
    ]
