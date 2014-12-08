# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='APIKey',
            fields=[
                ('key', models.CharField(primary_key=True, serialize=False, max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='auth_apikey')),
                ('email', models.CharField(null=True, blank=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
