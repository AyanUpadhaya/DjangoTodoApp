# Generated by Django 4.0.4 on 2022-04-22 15:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_text', models.CharField(max_length=500)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 4, 22, 15, 2, 18, 697789, tzinfo=utc))),
            ],
        ),
    ]
