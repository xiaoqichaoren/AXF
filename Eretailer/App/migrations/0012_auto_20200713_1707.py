# Generated by Django 2.2.13 on 2020-07-13 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(upload_to='static/uploads/icons/%Y/%m/%d/'),
        ),
    ]
