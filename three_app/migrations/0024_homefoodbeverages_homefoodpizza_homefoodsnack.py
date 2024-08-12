# Generated by Django 5.0.6 on 2024-06-24 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('three_app', '0023_alter_commetus_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='homefoodbeverages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('header', models.CharField(max_length=100, null=True)),
                ('content', models.TextField()),
                ('price', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='homefoodpizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('header', models.CharField(max_length=100, null=True)),
                ('content', models.TextField()),
                ('price', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='homefoodsnack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('header', models.CharField(max_length=100, null=True)),
                ('content', models.TextField()),
                ('price', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]