# Generated by Django 3.2.3 on 2021-06-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_communityhike_trail'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityhike',
            name='time',
            field=models.CharField(default='9:00AM PST', max_length=50),
            preserve_default=False,
        ),
    ]
