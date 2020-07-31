# Generated by Django 2.2.13 on 2020-07-13 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=32, unique=True)),
                ('phone', models.CharField(max_length=16)),
                ('icon', models.ImageField(upload_to='icons/%Y/%m/%d/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
