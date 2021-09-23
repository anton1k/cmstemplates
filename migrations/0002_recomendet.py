# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cmstemplates.models


class Migration(migrations.Migration):

    dependencies = [
        ('cmstemplates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recomendet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('url', models.URLField(verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430')),
                ('icon', models.ImageField(upload_to=cmstemplates.models.get_file_path, verbose_name='\u0418\u043a\u043e\u043d\u043a\u0430')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u043e')),
            ],
            options={
                'verbose_name': '\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u044f',
                'verbose_name_plural': '\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0438',
            },
        ),
    ]
