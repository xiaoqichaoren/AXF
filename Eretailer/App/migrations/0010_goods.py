# Generated by Django 2.2.13 on 2020-07-10 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_foodtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField(default=1)),
                ('productimg', models.CharField(max_length=255)),
                ('productname', models.CharField(max_length=128)),
                ('productlongname', models.CharField(max_length=255)),
                ('isxf', models.BooleanField(default=False)),
                ('pmdesc', models.BooleanField(default=False)),
                ('specifics', models.CharField(max_length=64)),
                ('price', models.FloatField(default=1)),
                ('marketprice', models.FloatField(default=1)),
                ('categoryid', models.IntegerField(default=1)),
                ('childcid', models.IntegerField(default=1)),
                ('childcidname', models.CharField(max_length=128)),
                ('dealerid', models.IntegerField(default=1)),
                ('storenums', models.IntegerField(default=1)),
                ('productnum', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
    ]
