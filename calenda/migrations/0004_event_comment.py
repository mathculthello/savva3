# Generated by Django 2.1.2 on 2018-10-29 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calenda', '0003_auto_20181029_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
