# Generated by Django 2.1.7 on 2019-03-05 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0002_auto_20190107_0721'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='level',
            field=models.CharField(choices=[('intern', 'Intern'), ('standard', 'Standard'), ('senior', 'Senior'), ('experienced', 'Experienced'), ('exceptional', 'Exceptional')], default='standard', max_length=15),
        ),
    ]
