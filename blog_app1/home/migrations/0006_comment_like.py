# Generated by Django 3.1.1 on 2020-10-08 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201007_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.ManyToManyField(related_name='likes', to='home.Blog'),
        ),
    ]
