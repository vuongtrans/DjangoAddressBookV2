# Generated by Django 3.2.5 on 2021-08-01 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20210801_0418'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['last_name']},
        ),
    ]
