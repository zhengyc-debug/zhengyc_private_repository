# Generated by Django 3.1 on 2021-09-29 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_user_info_user_money'),
    ]

    operations = [
        migrations.AddField(
            model_name='lucky_award',
            name='award_rate',
            field=models.FloatField(default=0.01),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='user_money',
            field=models.IntegerField(default=0),
        ),
    ]
