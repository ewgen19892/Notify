"""Notify tasks."""
import logging

from django.conf import settings
from django.core.mail import send_mail

from notifications.models import Notification
from notify.celery import app


@app.task
def send_email(notification_id) -> None:
    """Send email to."""
    try:
        notification = Notification.objects.get(pk=notification_id)
    except Notification.DoesNotExist:
        logger = logging.getLogger("notify.task.send_email")
        logger.warning("Notification with ID {} not found.".format(notification_id))
        return

    if notification.completed:
        return

    subject = "Notification: {}".format(notification.title)
    message = "{}. {}".format(notification.description, notification.place)
    recipients = list(notification.recipients.values_list("email", flat=True))
    recipients.append(notification.owner.email)

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipients,
    )
