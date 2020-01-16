# Generated by Django 3.0.2 on 2020-01-16 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lawyer_email', models.CharField(default='john@doe.com', max_length=200, unique=True)),
                ('lawyer_name', models.CharField(default='john doe', max_length=200)),
                ('lawyer_mobile', models.CharField(default='0700000000', max_length=20, unique=True)),
                ('lawyer_experience', models.CharField(default='2 Years', max_length=200)),
                ('lawyer_info', models.TextField()),
            ],
            options={
                'verbose_name': 'Lawyer',
                'verbose_name_plural': 'Lawyers',
                'db_table': 'Lawyer_Table',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.CharField(max_length=200)),
                ('case_description', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Lawyer_Profile',
                'verbose_name_plural': 'Profiles',
                'db_table': 'Profile_Table',
            },
        ),
    ]
