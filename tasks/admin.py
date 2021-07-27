from django.contrib import admin
from tasks.models import Label, MyUser, Status, Task

admin.site.register((MyUser, Status, Label, Task))
