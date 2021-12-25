from django.db import models
import datetime
# the following lines added:
import datetime
from django.utils import timezone


class MailTypes(models.Model):
    desc_text = models.CharField(max_length=200)

    def __str__(self):
        return self.desc_text


class Mails(models.Model):
    mail_type = models.ForeignKey(MailTypes, on_delete=models.CASCADE)
    mail_number = models.CharField(max_length=100, null=True)
    mail_date = models.DateField(null=True)
    mail_title = models.CharField(max_length=100)
    mail_text = models.TextField(max_length=500, null=True, blank=True)
    mail_from = models.CharField(max_length=100, null=True, blank=True)
    mail_to = models.CharField(max_length=100, null=True, blank=True)
    mail_rec_date = models.DateField(null=True, blank=True)
    mail_scan = models.ImageField(null=True, upload_to="images/", blank=True)

    def __str__(self):
        return self.mail_title
