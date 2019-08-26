# Generated by Django 2.1.1 on 2019-08-02 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_data', '0013_auto_20190801_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parking_slot',
            name='limit',
        ),
        migrations.AddField(
            model_name='parking_slot',
            name='lh',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parking_slot',
            name='lm',
            field=models.PositiveIntegerField(default=30),
        ),
    ]