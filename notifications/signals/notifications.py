"""Notification signals."""
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from celery.result import AsyncResult
from notifications.models import Notification
from notify.tasks import send_email


@receiver(post_save, sender=Notification)
def create_update_notification(sender, instance, created, **kwargs) -> None:
    """
    Create or update notification.

    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return: None
    """
    if created:
        task_id = send_email.apply_async(
            (instance.id,),
            eta=instance.date,
        ).id
        instance.task_id = task_id
        instance.save()
        return

    if instance.task_id:
        AsyncResult(instance.task_id).revoke()
    task_id = send_email.apply_async((instance.id,), eta=instance.date).id
    qs = Notification.objects.filter(id=instance.id)
    qs.update(task_id=task_id)


@receiver(pre_delete, sender=Notification)
def delete_notification(sender, instance, **kwargs) -> None:
    """
    Delete notification.

    :param sender:
    :param instance:
    :param kwargs:
    :return: None
    """
    if instance.task_id:
        AsyncResult(instance.task_id).revoke()
