# Generated by Django 2.2.6 on 2019-10-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20191009_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address_street_name',
            field=models.CharField(max_length=50),
        ),
    ]