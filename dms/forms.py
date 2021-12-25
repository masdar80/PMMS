from bootstrap_datepicker_plus.widgets import DateTimePickerInput, DatePickerInput, TimePickerInput, MonthPickerInput, \
    YearPickerInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column

from .models import *
from django import forms
from django.forms import ModelForm, DateInput

from django.views.generic import CreateView


class MailForm2(forms.ModelForm):
    class Meta:
        model = Mails
        fields = ['mail_type', 'mail_number', 'mail_date', 'mail_title', 'mail_text', 'mail_from', 'mail_to',
                 'mail_rec_date', 'mail_scan']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'حفظ'))


class MailForm(forms.ModelForm):
    class Meta:
        model = Mails
        fields = ['mail_type', 'mail_number', 'mail_date', 'mail_title', 'mail_text', 'mail_from', 'mail_to',
                  'mail_rec_date', 'mail_scan']
        widgets = {
            'mail_date': DatePickerInput().start_of('event days'),
            'mail_rec_date': DatePickerInput().start_of('event days'),
        }
        labels = {
            "mail_type": "نوع البريد",
            "mail_number": "رقم",
            "mail_date": "تاريخ",
            "mail_title": "عنوان",
            "mail_text": "توصيف",
            "mail_from": "من",
            "mail_to": "إلى",
            "mail_rec_date": "تاريخ الاستلام",
            "mail_scan": "تحميل صورة البريد"
        }




