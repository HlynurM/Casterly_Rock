# Generated by Django 2.2.1 on 2019-05-15 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estates', '0003_auto_20190514_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='starrating',
            name='has_star',
            field=models.BooleanField(default=None),
        ),
    ]