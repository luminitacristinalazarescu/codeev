# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_create_project_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='difficulty',
            field=models.CharField(choices=[('beginner', 'beginner'), ('intermediate', 'intermediate'), ('advanced', 'advanced')], max_length=15),
        ),
    ]
