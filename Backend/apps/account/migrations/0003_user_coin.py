# Generated by Django 2.2.4 on 2019-09-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190908_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='coin',
            field=models.BigIntegerField(default=10),
        ),
    ]
