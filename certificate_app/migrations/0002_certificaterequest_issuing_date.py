# Generated by Django 4.2.5 on 2023-09-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificaterequest',
            name='issuing_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]