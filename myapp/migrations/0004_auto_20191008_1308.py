# Generated by Django 2.2.6 on 2019-10-08 13:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20191008_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contact_name',
            field=models.CharField(max_length=48, validators=[django.core.validators.RegexValidator('^\\d{a,z}$')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='state',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\d{a,z}$')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='suburb',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator('^\\d{a,z}$')]),
        ),
    ]