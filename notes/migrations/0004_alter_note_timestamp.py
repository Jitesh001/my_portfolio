# Generated by Django 4.2.6 on 2023-10-27 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_note_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 27, 12, 32, 44, 495361, tzinfo=datetime.timezone.utc)),
        ),
    ]
