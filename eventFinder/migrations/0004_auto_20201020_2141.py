# Generated by Django 3.1.1 on 2020-10-20 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinder', '0003_event_event_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_time',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
