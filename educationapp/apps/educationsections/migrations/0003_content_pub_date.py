# Generated by Django 3.0.5 on 2020-04-25 17:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('educationsections', '0002_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 17, 2, 26, 290948, tzinfo=utc), verbose_name='дата публикации'),
            preserve_default=False,
        ),
    ]
