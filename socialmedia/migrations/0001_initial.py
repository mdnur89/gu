# Generated by Django 2.1.4 on 2018-12-10 16:18

from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('newsroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wait_time', models.PositiveIntegerField(help_text='Number of minutes after publication till tweet.')),
                ('status', models.CharField(choices=[('scheduled', 'Scheduled'), ('sent', 'Sent'), ('failed', 'Failed'), ('paused', 'Paused')], default='scheduled', max_length=20)),
                ('tweet_text', models.CharField(blank=True, max_length=117)),
                ('image', filebrowser.fields.FileBrowseField(blank=True, max_length=200)),
                ('characters_left', models.IntegerField(default=116)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsroom.Article')),
            ],
            options={
                'ordering': ['article__published', 'wait_time'],
            },
        ),
        migrations.CreateModel(
            name='TwitterHandle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Twitter handle',
                'ordering': ['name'],
                'verbose_name_plural': 'Twitter Handles',
            },
        ),
        migrations.AddField(
            model_name='tweet',
            name='tag_accounts',
            field=models.ManyToManyField(blank=True, to='socialmedia.TwitterHandle'),
        ),
    ]
