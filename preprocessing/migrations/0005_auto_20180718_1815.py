# Generated by Django 2.0.7 on 2018-07-18 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preprocessing', '0004_auto_20180718_1257'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ('-id',)},
        ),
    ]