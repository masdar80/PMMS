# Generated by Django 4.0 on 2021-12-17 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0003_alter_mails_mail_scan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mails',
            name='mail_text',
            field=models.TextField(max_length=500),
        ),
    ]
