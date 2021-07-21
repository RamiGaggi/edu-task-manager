import django_filters
from django import forms
from django.utils.translation import gettext as _
from tasks.models import Label, Status, Task


def get_status_choices():
    """asdas."""
    return [(status.id, status.name) for status in Status.objects.all()]


def get_label_choices():
    """asdas."""
    return [(label.id, label.name) for label in Label.objects.all()]


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(
        choices=get_status_choices(),
        label=_('Статус'),
    )
    labels = django_filters.ChoiceFilter(
        choices=get_label_choices(),
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
