# Generated by Django 2.2.1 on 2019-05-16 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20190516_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
