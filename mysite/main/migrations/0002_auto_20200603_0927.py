# Generated by Django 3.0.6 on 2020-06-03 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial_category',
            old_name='categogary_summary',
            new_name='category_summary',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 3, 9, 26, 47, 332485), verbose_name='date published'),
        ),
    ]