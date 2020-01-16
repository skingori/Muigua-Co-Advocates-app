from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Lawyer(models.Model):
    lawyer_username = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    lawyer_mobile = models.CharField(max_length=20, default='0700000000', unique=True)
    lawyer_experience = models.CharField(max_length=200, default='2 Years')
    lawyer_info = models.TextField()

    def __str__(self):
        return self.lawyer_username

    class Meta:
        verbose_name = 'Lawyer'
        verbose_name_plural = 'Lawyers'
        db_table = 'Lawyer_Table'


class Clients(models.Model):
    client_username = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    client_mobile = models.CharField(max_length=20, default='0700000000', unique=True)
    client_age = models.CharField(max_length=200, default='2 Years')
    client_info = models.TextField()

    def __str__(self):
        return self.client_username

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = 'Clients'
        db_table = 'Client_Table'


class Cases(models.Model):
    case_title = models.CharField(max_length=200)
    case_owner = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    case_unique_key = models.CharField(max_length=200, unique=True)
    case_description = models.TextField()
    ACCEPT = '1'
    REJECT = '2'
    WAIT = '3'
    CHOICES = [
        (ACCEPT, 'Accepted'),
        (REJECT, 'Rejected'),
        (WAIT, 'Awaiting'),
    ]
    case_status = models.CharField(choices=CHOICES, default=WAIT, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.case_title

    class Meta:
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'
        db_table = 'Case_Table'


class RePresentation(models.Model):
    Represented_by = models.OneToOneField(Lawyer, on_delete=models.SET_NULL, null=True)
    Represented_user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    presented_to = models.CharField(max_length=200)
    presentation_court = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s Case Represented by %s" % (self.Represented_user, self.Represented_by)

    class Meta:
        verbose_name = 'Case Re-Presentation'
        verbose_name_plural = 'Case (s) Re-Presentation'
        db_table = 'Representation_Table'


class Appearance(models.Model):
    Appearing_lawyer = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    Appearance_court = models.CharField(max_length=200)
    Appearance_date = models.DateTimeField()
    WAS_PRESENT = '1'
    NOT_PRESENT = '2'
    CASE_CLOSED = '3'
    CHOICES = [
        (WAS_PRESENT, 'Present'),
        (NOT_PRESENT, 'Absent'),
        (CASE_CLOSED, 'Closed'),
    ]
    Appearance_status = models.CharField(choices=CHOICES, default=NOT_PRESENT, max_length=10)
    Appearance_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s appeared on %s" % (self.Appearing_lawyer, self.Appearance_date)

    class Meta:
        verbose_name = 'Court Appearance'
        verbose_name_plural = 'Court Appearances'
        db_table = 'Appearance_Table'
