from django.contrib.auth.models import User
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


class Label(TimeStampMixin):
    name = models.CharField(max_length=256, unique=True, verbose_name=_('Имя'))

    def __str__(self):
        return self.name


class Task(TimeStampMixin):
    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name=_('Имя'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Описание'),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Автор'),
        related_name='author_id',
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        verbose_name=_('Статус'),
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='executor_id',
        verbose_name=_('Исполнитель'),
    )
    labels = models.ManyToManyField(Label, blank=True)

    def __str__(self):
        return self.name
