# Generated by Django 3.1.4 on 2020-12-09 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0005_auto_20201209_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='name',
            new_name='tutorial_name',
        ),
    ]
