# Generated by Django 2.2.1 on 2019-05-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_userprofile_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='street',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]