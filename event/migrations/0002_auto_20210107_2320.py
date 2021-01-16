# Generated by Django 3.1.4 on 2021-01-07 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantreg',
            name='Deadline',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='participantreg',
            name='Location',
            field=models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], default='Online', max_length=7),
        ),
        migrations.AlterField(
            model_name='participantreg',
            name='RegFrom',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='participantreg',
            name='RegTo',
            field=models.DateTimeField(),
        ),
    ]