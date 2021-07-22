from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/create/', views.UserRegistrationView.as_view(), name='user-create'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user-delete'),

    path('statuses/', views.StatusListView.as_view(), name='status-list'),
    path('statuses/create/', views.StatusCreateView.as_view(), name='status-create'),
    path('statuses/<int:pk>/update/', views.StatusUpdateView.as_view(), name='status-update'),
    path('statuses/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status-delete'),

    path('tasks/', views.TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskView.as_view(), name='task'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),

    path('labels/', views.LabelListView.as_view(), name='label-list'),
    path('labels/create/', views.LabelCreateView.as_view(), name='label-create'),
    path('labels/<int:pk>/update/', views.LabelUpdateView.as_view(), name='label-update'),
    path('labels/<int:pk>/delete/', views.LabelDeleteView.as_view(), name='label-delete'),
]
