from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from tasks.misc import MyLoginRequiredMixin, add_denied_message_and_redirect
from tasks.models import Task


class TaskView(MyLoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task_info'
    template_name = 'tasks/task.html'


class TaskListView(MyLoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'tasks/task_list.html'


class TaskCreateView(MyLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor']
    template_name = 'tasks/task_create.html'
    success_message = _('Задача успешно создана')
    success_url = reverse_lazy('tasks:task-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(MyLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('tasks:task-list')
    success_message = _('Задача успешно изменена')
    fields = ['name', 'description', 'status', 'executor']


class TaskDeleteView(MyLoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks:task-list')

    def delete(self, request, *args, **kwargs):
        """Add success message fo delete."""
        success_message = _('Задача успешно удалена')
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().delete(request, *args, **kwargs)

    @add_denied_message_and_redirect(
        redirect_url='tasks:task-list',
        message=_('Задачу может удалить только её автор'),
    )
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.id == self.get_object().author.id:
            return super().dispatch(request, *args, **kwargs)
