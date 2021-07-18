from django.db import models
from django.utils.translation import gettext as _


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата создания'),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Дата изменения'),
    )

    class Meta:
        abstract = True


class Status(TimeStampMixin):
    name = models.CharField(max_length=256, unique=True, verbose_name=_('Имя'))

    def __str__(self):
        return self.name
