# Generated by Django 2.2.2 on 2019-06-28 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='edad',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]