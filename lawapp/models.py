from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Lawyer(models.Model):
    lawyer_username = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    lawyer_mobile = models.CharField(max_length=20, default='0700000000', unique=True)
    lawyer_experience = models.CharField(max_length=200, default='2 Years')
    lawyer_info = models.TextField()

    def __str__(self):
        return str(self.lawyer_username)

    class Meta:
        verbose_name = 'Lawyer'
        verbose_name_plural = 'Lawyers'
        db_table = 'Lawyer_Table'


class Clients(models.Model):
    client_username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    client_mobile = models.CharField(max_length=20, default='0700000000', unique=True)
    DEFENDANT = 'defendant'
    PLAINTIFF = 'plaintiff'
    OTHER = 'other'
    PARTY = [
        (DEFENDANT, 'Defendant'),
        (PLAINTIFF, 'Plaintiff'),
        (OTHER, 'Other'),
    ]
    client_party = models.CharField(choices=PARTY, max_length=20, default=OTHER)
    client_age = models.CharField(max_length=200, default='2 Years')
    Other_information = models.TextField()

    def __str__(self):
        return str(self.client_username)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = 'Clients'
        db_table = 'Client_Table'


class Cases(models.Model):
    case_title = models.CharField(max_length=200)
    case_owner_username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, unique=False)
    case_unique_key = models.CharField(max_length=200, unique=True, primary_key=True)
    case_document = models.FileField()
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
        return "%s Completed Successfully!" % self.case_title

    class Meta:
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'
        db_table = 'Case_Table'


class Courts(models.Model):
    court_name = models.CharField(max_length=20)
    court_location = models.CharField(max_length=20)
    court_address = models.CharField(max_length=100)
    court_description = models.TextField()

    def __str__(self):
        return "%s" % self.court_name

    class Meta:
        verbose_name = 'Court'
        verbose_name_plural = 'Courts'
        db_table = 'Courts_Table'


class RePresentation(models.Model):
    Represented_by = models.ForeignKey(Lawyer, on_delete=models.SET_NULL, unique=False, null=True)
    Represented_user = models.ForeignKey(Clients, on_delete=models.SET_NULL, unique=False, null=True)
    presented_to = models.CharField(max_length=200)
    presentation_court = models.ForeignKey(Courts, on_delete=models.SET_NULL, max_length=200, null=True, unique=False)
    Description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s Case Represented by %s" % (self.Represented_user, self.Represented_by)

    class Meta:
        verbose_name = 'Case Re-Presentation'
        verbose_name_plural = 'Case Re-Presentation'
        db_table = 'Representation_Table'


class Appearance(models.Model):
    Appearing_lawyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, unique=False)
    Appearance_court = models.ForeignKey(Courts, on_delete=models.SET_NULL, null=True, unique=False)
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

