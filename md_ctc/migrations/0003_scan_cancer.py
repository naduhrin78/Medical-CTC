# Generated by Django 2.0.7 on 2018-07-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('md_ctc', '0002_scan'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='cancer',
            field=models.IntegerField(default=0),
        ),
    ]
