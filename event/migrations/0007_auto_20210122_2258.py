# Generated by Django 3.1.4 on 2021-01-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_remove_participantreg_eventnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantreg',
            name='Location',
            field=models.CharField(max_length=7),
        ),
    ]
