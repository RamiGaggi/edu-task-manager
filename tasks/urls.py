from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('users', views.UserListView.as_view(), name='user-list'),
    path('users/create', views.UserRegistrationView.as_view(), name='user-create'),
    path('login', views.UserLoginView.as_view(), name='user-login'),
    path('logout', views.UserLogoutView.as_view(), name='logout'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user-delete'),
    path('statuses', views.StatusListView.as_view(), name='status-list'),
    path('statuses/create', views.StatusCreateView.as_view(), name='status-create'),
    path('statuses/<int:pk>/update', views.StatusUpdateView.as_view(), name='status-update'),
    path('statuses/<int:pk>/delete', views.StatusDeleteView.as_view(), name='status-delete'),
]
