# Generated by Django 3.1 on 2020-10-22 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_auto_20201023_0119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sluug',
            new_name='slug',
        ),
    ]
