import django_filters
from django import forms
from django.utils.translation import gettext as _
from tasks.models import Label, Status, Task

STATUS_CHOICES = [(status.id, status.name) for status in Status.objects.all()]  # noqa: WPS407, E501
LABEL_CHOICES = [  # noqa: WPS407
    (label.id, label.name) for label in Label.objects.all()
]
AUTHOR_CHOICES = (
    (True, 'True'),
    (0, 'fdghfgh'),
)


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(
        choices=STATUS_CHOICES,
        label=_('Статус'),
    )
    labels = django_filters.ChoiceFilter(
        choices=LABEL_CHOICES,
        label=_('Метка'),
    )
    author_id = django_filters.BooleanFilter(
        method='filter_current_user_tasks',
        label=_('Только свои задачи'),
        widget=forms.CheckboxInput,
    )

    def filter_current_user_tasks(self, queryset, name, checkbox):
        user_id = self.request.user.id
        return queryset.filter(**{name: user_id}) if checkbox else queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
