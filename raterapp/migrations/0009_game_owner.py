# Generated by Django 3.2.1 on 2021-05-15 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raterapp', '0008_auto_20210514_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='raterapp.user'),
            preserve_default=False,
        ),
    ]
