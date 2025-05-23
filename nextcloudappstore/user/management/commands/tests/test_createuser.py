"""
SPDX-FileCopyrightText: 2017 Nextcloud GmbH and Nextcloud contributors
SPDX-License-Identifier: AGPL-3.0-or-later
"""

from io import StringIO

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase


class CreateUserCommandTest(TestCase):
    def test_create_user(self):
        call_command(
            "createtestuser", "--username=cmdtest", "--password=cmdtest", "--email=test@test.com", stdout=StringIO()
        )
        user = get_user_model().objects.get(username="cmdtest")
        self.assertEqual("test@test.com", user.email)
