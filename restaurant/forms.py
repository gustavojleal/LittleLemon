from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text="Minimum 8 characters. Cannot be a common or all-numeric password."
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        # Validate password match
        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match!")

        return cleaned_data