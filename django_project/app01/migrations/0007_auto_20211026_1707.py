# Generated by Django 3.1 on 2021-10-26 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20210929_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='user_name',
            field=models.CharField(max_length=255),
        ),
    ]
