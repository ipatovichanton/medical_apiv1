# Generated by Django 3.0.8 on 2020-08-03 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0009_add_subregion'),
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pharmacies',
            new_name='Pharmacy',
        ),
    ]