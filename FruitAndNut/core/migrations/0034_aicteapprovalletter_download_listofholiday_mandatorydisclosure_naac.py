# Generated by Django 2.1.1 on 2018-12-07 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20181207_0717'),
    ]

    operations = [
        migrations.CreateModel(
            name='AicteApprovalLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.FileField(upload_to='files/aicte_approval_letter/%Y-%m-%d--%H:%M:%S')),
            ],
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ListOfHoliday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.FileField(upload_to='files/list_of_holidays/%Y-%m-%d--%H:%M:%S')),
            ],
        ),
        migrations.CreateModel(
            name='MandatoryDisclosure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.FileField(upload_to='files/mandatory_disclosure/%Y-%m-%d--%H:%M:%S')),
            ],
        ),
        migrations.CreateModel(
            name='Naac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.FileField(upload_to='files/naac/%Y-%m-%d--%H:%M:%S')),
            ],
        ),
    ]