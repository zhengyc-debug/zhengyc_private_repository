# Generated by Django 3.1 on 2021-01-27 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='user_sex',
            field=models.CharField(choices=[(1, '男'), (0, '女')], default=1, max_length=2),
        ),
    ]
