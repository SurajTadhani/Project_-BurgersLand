# Generated by Django 5.0.6 on 2024-08-10 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('three_app', '0045_alter_booking_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='homefoodblog',
            name='category',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homefoodblog',
            name='message',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homefoodblog',
            name='username',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
    ]