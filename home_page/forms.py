from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    designation = forms.CharField(required=True)

    class Meta:
        model = User
        fields = {"username",
                  "email",
                  "password1",
                  "password2",
                  "designation"}

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
