# Generated by Django 4.0 on 2021-12-19 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0007_delete_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='mails',
            name='mail_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mails',
            name='mail_from',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mails',
            name='mail_scan',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='mails',
            name='mail_text',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='mails',
            name='mail_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mails',
            name='mail_to',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
