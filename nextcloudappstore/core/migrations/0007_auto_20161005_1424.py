# Generated by Django 1.10.2 on 2016-10-05 14:24
#
#SPDX-FileCopyrightText: 2016 Nextcloud GmbH and Nextcloud contributors
#SPDX-License-Identifier: AGPL-3.0-or-later

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_apprelease_changelog'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppReleaseTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('changelog', models.TextField(default='', help_text='The release changelog. Can contain Markdown', verbose_name='Changelog')),
            ],
            options={
                'default_permissions': (),
                'verbose_name': 'App release Translation',
                'db_table': 'core_apprelease_translation',
                'db_tablespace': '',
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='apprelease',
            name='changelog',
        ),
        migrations.AddField(
            model_name='appreleasetranslation',
            name='master',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='core.AppRelease'),
        ),
        migrations.AlterUniqueTogether(
            name='appreleasetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
