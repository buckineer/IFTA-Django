# Generated by Django 3.2 on 2022-02-23 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck_management_app', '0009_quarter_fuel_tax_owned'),
    ]

    operations = [
        migrations.AddField(
            model_name='quarter',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
    ]