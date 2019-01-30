# Generated by Django 2.1.1 on 2019-01-30 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_auto_20190130_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='file',
            field=models.FileField(blank=True, upload_to='files/notification//%Y-%m-%d'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='link',
            field=models.URLField(blank=True, max_length=250),
        ),
    ]
