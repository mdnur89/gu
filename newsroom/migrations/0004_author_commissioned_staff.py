# Generated by Django 2.1.7 on 2019-04-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0003_author_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='commissioned_staff',
            field=models.BooleanField(default=False),
        ),
    ]
