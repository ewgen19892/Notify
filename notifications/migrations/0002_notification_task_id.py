# Generated by Django 2.2.6 on 2019-10-27 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='task_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]