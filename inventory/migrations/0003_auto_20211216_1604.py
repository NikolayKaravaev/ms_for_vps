# Generated by Django 3.2.9 on 2021-12-16 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20211215_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='quality',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='units',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
