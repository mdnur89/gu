# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-08 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0062_auto_20171218_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='copyright',
            field=models.TextField(blank=True, default='&copy; 2018 GroundUp. <a rel="license" href="http://creativecommons.org/licenses/by-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="/static/newsroom/images/cc.png" /></a><br />This article is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nd/4.0/">Creative Commons Attribution-NoDerivatives 4.0 International License</a>.<p>You may republish this article, so long as you credit the authors and GroundUp, and do not change the text. Please include a link back to the original article.</p>'),
        ),
    ]
