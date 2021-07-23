from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from tasks.models import MyUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = [
            'first_name',
            'last_name',
            'username',
        ]


class UserUpdateForm(forms.ModelForm):

    password1 = forms.CharField(
        label=_('Пароль'),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_('Подтверждение пароля'),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_('Для подтверждения введите, пожалуйста, пароль ещё раз.'),
    )

    def validation(self, cleaned_data):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError(_('Введенные пароли не совпадают.'))
        password_validation.validate_password(self.cleaned_data['password1'])

    def clean(self):
        cleaned_data = super().clean()
        self.validation(cleaned_data)
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = MyUser
        fields = ['username', 'first_name', 'last_name']
