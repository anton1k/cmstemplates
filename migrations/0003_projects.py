# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cmstemplates.models


class Migration(migrations.Migration):

    dependencies = [
        ('cmstemplates', '0002_recomendet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('logo', models.ImageField(upload_to=cmstemplates.models.get_file_path, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('url', models.URLField(verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u043e')),
                ('sorting', models.IntegerField(default=100, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430', blank=True)),
            ],
            options={
                'ordering': ['sorting', 'pk'],
                'verbose_name': '\u0421\u043f\u0435\u0446\u043f\u0440\u043e\u0435\u043a\u0442',
                'verbose_name_plural': '\u0421\u043f\u0435\u0446\u043f\u0440\u043e\u0435\u043a\u0442\u044b',
            },
        ),
    ]
