# Generated by Django 3.0.8 on 2020-07-28 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0009_add_subregion'),
        ('clinics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='address',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clinic',
            name='city',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='cities_light.City'),
            preserve_default=False,
        ),
    ]
