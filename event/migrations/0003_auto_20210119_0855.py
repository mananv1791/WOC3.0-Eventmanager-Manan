# Generated by Django 3.1.4 on 2021-01-19 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20210107_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantreg',
            name='EventName',
            field=models.CharField(max_length=300),
        ),
    ]
