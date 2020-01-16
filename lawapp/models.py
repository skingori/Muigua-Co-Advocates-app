from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Lawyer(models.Model):
    lawyer_email = models.CharField(max_length=200, default='john@doe.com', unique=True)
    lawyer_name = models.CharField(max_length=200, default='john doe')
    lawyer_mobile = models.CharField(max_length=20, default='0700000000', unique=True)
    lawyer_experience = models.CharField(max_length=200, default='2 Years')
    lawyer_info = models.TextField()

    def __str__(self):
        return self.lawyer_email

    class Meta:
        verbose_name = 'Lawyer'
        verbose_name_plural = 'Lawyers'
        db_table = 'Lawyer_Table'


# class UserProfile(models.Model):
#     # This field is required.
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Other fields here
#     case = models.CharField(max_length=200)
#     case_description = models.TextField()
#
#     class Meta:
#         verbose_name = 'Lawyer Profile'
#         verbose_name_plural = 'Profiles'
#         db_table = 'Profile_Table'
