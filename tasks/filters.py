import django_filters
from django import forms
from django.utils.translation import gettext as _
from tasks.models import Label, Status, Task


class TaskFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        """Update filters after creating status/labels."""
        super().__init__(*args, **kwargs)
        self.filters['status'].extra['choices'] = [(status.id, status.name) for status in Status.objects.all()]  # noqa: E501
        self.filters['status']._label = _('Статус')
        self.filters['labels'].extra['choices'] = [(label.id, label.name) for label in Label.objects.all()]  # noqa: E501
        self.filters['labels']._label = _('Метка')
        self.filters['author_id']._label = _('Только свои задачи')
        self.filters['executor']._label = _('Исполнитель')

    status = django_filters.ChoiceFilter(
        choices=[],
        label='',
    )
    labels = django_filters.ChoiceFilter(
        choices=[],
        label='',
    )
    author_id = django_filters.BooleanFilter(
        method='filter_current_user_tasks',
        label='',
        widget=forms.CheckboxInput,
    )

    def filter_current_user_tasks(self, queryset, name, checkbox):
        user_id = self.request.user.id
        return queryset.filter(**{name: user_id}) if checkbox else queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
