from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.UserListView.as_view(), name='user-list'),
    path('users/create', views.UserCreateView.as_view(), name='user-create'),
    path('login', views.login, name='user-login'),
]
