"""
SPDX-FileCopyrightText: 2017 Nextcloud GmbH and Nextcloud contributors
SPDX-License-Identifier: AGPL-3.0-or-later
"""

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Sets the password "admin" for the user "admin". Only use this in development!'

    def handle(self, *args, **options):
        user = get_user_model().objects.get(username="admin")
        user.set_password("admin")
        user.save()
        msg = "Successfully set password {} for user {}".format("admin", "admin")
        self.stdout.write(self.style.SUCCESS(msg))
