# Generated by Django 1.11.10 on 2018-02-17 09:46
#
#SPDX-FileCopyrightText: 2018 Nextcloud GmbH and Nextcloud contributors
#SPDX-License-Identifier: AGPL-3.0-or-later

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_nextcloudrelease_has_release'),
    ]

    operations = [
        migrations.AddField(
            model_name='nextcloudrelease',
            name='is_supported',
            field=models.BooleanField(default=False, help_text='True if this version is still officially supported (excluding enterprise support)', verbose_name='Version is supported'),
        ),
    ]
