# Generated by Django 4.1.7 on 2023-04-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aqzhol', '0003_remove_statistics_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='second',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
