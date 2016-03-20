# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, default='')),
                ('body', models.TextField(default='')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(to='article.Article'),
        ),
    ]
