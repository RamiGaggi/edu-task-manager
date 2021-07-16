
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        """."""

        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
        ]


class UserUpdateForm(UserChangeForm):
    class Meta:
        """."""

        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
        ]
