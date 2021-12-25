from django.contrib import admin
from .models import Mails
from .models import MailTypes

admin.site.register(Mails)
admin.site.register(MailTypes)
# Register your models here.
