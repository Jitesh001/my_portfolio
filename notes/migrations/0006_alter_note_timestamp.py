# Generated by Django 4.2.6 on 2023-10-27 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_alter_note_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 27, 18, 6, 20, 466619, tzinfo=datetime.timezone.utc)),
        ),
    ]
