# Generated by Django 3.1.2 on 2020-10-25 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ayewa', '0023_auto_20201025_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indexpage',
            name='nav_description',
        ),
    ]
