# Generated by Django 2.2.6 on 2019-10-09 10:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20191009_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='postcode',
            field=models.CharField(max_length=6, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]
