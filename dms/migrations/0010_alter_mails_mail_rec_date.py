# Generated by Django 4.0 on 2021-12-19 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0009_mails_mail_rec_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mails',
            name='mail_rec_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]