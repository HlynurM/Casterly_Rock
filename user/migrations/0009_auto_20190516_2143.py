# Generated by Django 2.2.1 on 2019-05-16 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20190516_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.CharField(blank=True, max_length=999),
        ),
    ]
