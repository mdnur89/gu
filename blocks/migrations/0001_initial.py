# Generated by Django 2.1.4 on 2018-12-10 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('html', models.TextField(blank=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BlockGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveSmallIntegerField(null=True, verbose_name='position')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_to_group', to='blocks.Block')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('pages_include', models.TextField(blank=True)),
                ('pages_exclude', models.TextField(blank=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('blocks', models.ManyToManyField(blank=True, through='blocks.BlockGroup', to='blocks.Block')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='blockgroup',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blocks.Group'),
        ),
    ]
