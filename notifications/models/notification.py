"""Notification."""
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Notification(models.Model):
    """Notification model."""

    owner = models.ForeignKey(
        verbose_name=_("Owner"),
        to=User,
        on_delete=models.CASCADE,
        related_name="notifications",
    )
    title = models.CharField(verbose_name=_("Title"), max_length=155)
    description = models.TextField(verbose_name=_("Description"))
    place = models.CharField(verbose_name=_("Place"), max_length=155)
    recipients = models.ManyToManyField(
        User,
        related_name="recipients",
        blank=True
    )
    create_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(verbose_name=_("Date"))
    completed = models.BooleanField(default=False)
    task_id = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        """
        Call as string.

        :return: Self owner email and title
        """
        return "{} {}".format(self.owner.email, self.title)

    class Meta:
        """Meta."""

        ordering = ("-pk",)
