"""
SPDX-FileCopyrightText: 2017 Nextcloud GmbH and Nextcloud contributors
SPDX-License-Identifier: AGPL-3.0-or-later
"""

from allauth.account.models import EmailAddress
from allauth.account.signals import email_confirmed
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.translation import gettext as _
from rest_framework.authtoken.models import Token

from nextcloudappstore.user.facades import update_token
from nextcloudappstore.user.models import UserProfile

from .odoo import subscribe_user_to_news


@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid="create_token")
def post_save_create_token(sender, **kwargs):
    if kwargs["created"]:
        t = Token.objects.create(user=kwargs["instance"])
        t.save()


@receiver(pre_save, sender=get_user_model())
def password_changed_signal(sender, instance, **kwargs):
    """
    Regenerate token on password change
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    mail_subect = _("Nextcloud app store password changed")
    mail_message = _("Your Nextcloud app store password has changed. Contact support if this was not you.")

    try:
        user = get_user_model().objects.get(pk=instance.pk)
        if user.password != instance.password and instance._password is not None:
            # make sure we only send an email when user changed their
            # password and _password is set and not when password hash
            # was changed due to a new default hashing algorithm
            update_token(user.username)
            send_mail(mail_subect, mail_message, settings.DEFAULT_FROM_EMAIL, [user.email], False)
    except User.DoesNotExist:
        pass


@receiver(email_confirmed)
def handle_email_confirmation(request, email_address, **kwargs):
    user = email_address.user
    try:
        # Mark the new email address as the user's primary email
        email_address.set_as_primary()
        # Delete any other email addresses belonging to the user
        EmailAddress.objects.filter(user=user).exclude(primary=True).delete()

        # Get the user's profile
        user_profile = UserProfile.objects.get(user=user)
        # Check if the user has opted in for news
        if user_profile.subscribe_to_news:
            subscribe_user_to_news(email_address.email, "")
    except UserProfile.DoesNotExist:
        print(f"UserProfile not found for user: {user.id}")
    except Exception as e:
        print(f"An error occurred: {e}")
