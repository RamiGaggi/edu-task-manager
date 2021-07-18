from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from tasks.misc import MyLoginRequiredMixin
from tasks.models import Status


class StatusListView(MyLoginRequiredMixin, ListView):
    model = Status
    context_object_name = 'status_list'
    template_name = 'tasks/status_list.html'


class StatusCreateView(MyLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = 'tasks/status_create.html'
    success_message = _('Статус успешно создан')

    def get_success_url(self):
        """Get url after registration."""
        return reverse('tasks:status-list')


class StatusUpdateView(MyLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    template_name = 'tasks/status_update.html'
    success_url = reverse_lazy('tasks:status-list')
    success_message = _('Статус успешно изменён')
    fields = ['name']


class StatusDeleteView(MyLoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'tasks/status_delete.html'
    success_url = reverse_lazy('tasks:status-list')

    def delete(self, request, *args, **kwargs):
        """Add success message fo delete."""
        success_message = _('Статус успешно удалён')
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().delete(request, *args, **kwargs)
