# Generated by Django 2.1.7 on 2019-04-22 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0003_auto_20190421_1909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='target',
            options={'ordering': ['-number']},
        ),
        migrations.AddField(
            model_name='target',
            name='public_solution',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='target',
            name='number',
            field=models.PositiveSmallIntegerField(default=0, editable=False),
        ),
    ]