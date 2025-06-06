"""
SPDX-FileCopyrightText: 2023 Nextcloud GmbH and Nextcloud contributors
SPDX-License-Identifier: AGPL-3.0-or-later
"""

from time import sleep

from django.test import tag

from nextcloudappstore.core.tests.e2e.base import BaseStoreTest


@tag("e2e")
class ResetPasswordTest(BaseStoreTest):
    def test_reset_pass(self):
        self.go_to("account_reset_password")
        email_input = self.by_id("id_email")
        email_input.clear()
        email_input.send_keys("admin@admin.com")
        email_input.submit()
        self.wait_for_url("/password/reset/done")

        self.go_to("account_reset_password")
        email_input = self.by_id("id_email")
        email_input.clear()
        email_input.send_keys("admin@admin.com")
        email_input.submit()
        sleep(4)  # wait till url change
        self.wait_for_url_match(r".*\/password\/reset\/?$", timeout=5)
