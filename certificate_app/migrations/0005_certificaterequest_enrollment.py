# Generated by Django 4.2.5 on 2023-09-17 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificate_app', '0004_alter_certificaterequest_issuing_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificaterequest',
            name='enrollment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='certificate_app.enrollment'),
            preserve_default=False,
        ),
    ]