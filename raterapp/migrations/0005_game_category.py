# Generated by Django 3.2.1 on 2021-05-12 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raterapp', '0004_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.ManyToManyField(through='raterapp.CategoryGame', to='raterapp.Game'),
        ),
    ]