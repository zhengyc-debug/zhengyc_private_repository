# Generated by Django 3.1 on 2021-10-28 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_user_stores'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_stores',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.user_info'),
        ),
        migrations.AlterField(
            model_name='user_stores',
            name='stores_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.lucky_award'),
        ),
    ]