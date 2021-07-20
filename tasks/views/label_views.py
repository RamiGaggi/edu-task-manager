from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from tasks.misc import MyLoginRequiredMixin
from tasks.models import Label


class LabelListView(MyLoginRequiredMixin, ListView):
    model = Label
    context_object_name = 'label_list'
    template_name = 'labels/label_list.html'


class LabelCreateView(MyLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    fields = ['name']
    template_name = 'tasks/label_create.html'
    success_message = _('Метка успешно создана')
    success_url = reverse_lazy('tasks:label-list')


class LabelUpdateView(MyLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    template_name = 'tasks/label_update.html'
    success_url = reverse_lazy('tasks:label-list')
    success_message = _('Метка успешно изменена')
    fields = ['name']


class LabelDeleteView(MyLoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'tasks/label_delete.html'
    success_url = reverse_lazy('tasks:label-list')

    def delete(self, request, *args, **kwargs):
        """Add success message fo delete."""
        success_message = _('Метка успешно удалена')
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().delete(request, *args, **kwargs)