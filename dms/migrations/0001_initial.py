# Generated by Django 4.0 on 2021-12-14 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_title', models.CharField(max_length=100)),
                ('mail_text', models.CharField(max_length=500)),
                ('mail_date', models.DateField()),
                ('mail_from', models.CharField(max_length=100)),
                ('mail_to', models.CharField(max_length=100)),
                ('mail_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dms.mailtypes')),
            ],
        ),
    ]
