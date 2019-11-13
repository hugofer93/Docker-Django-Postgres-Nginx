from django import forms
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from . import models


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField()

    class Meta:
        model = models.User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )


class SignInForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')

        try:
            if '@' in username:
                query = (
                    Q(username=username) |
                    Q(email=username)
                )
                # Query for username or email before of 'Sign In'
                user = models.User.objects.get(query)

                if user is not None:
                    self.cleaned_data['username'] = user.username

        except models.User.DoesNotExist:
            pass

        return super().clean()
