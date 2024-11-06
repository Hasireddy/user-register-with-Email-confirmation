from django import forms

from .models import User


class UserRegisterForm(forms.ModelForm):
    password2 = forms.CharField(
        required=True,
        max_length=200,
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm your password"}),
    )

    class Meta:
        model = User
        verbose_name = "user"
        exclude = ["is_active", "last_login"]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": "Enter your First name"}
            ),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter your Last name"}),
            "username": forms.TextInput(attrs={"placeholder": "Enter your Username"}),
            "email": forms.EmailInput(
                attrs={"placeholder": "Enter your Email address"}
            ),
            "password": forms.PasswordInput(
                attrs={"placeholder": "Enter your Password"}
            ),
        }

        labels = {
            "first_name": "First name",
            "last_name": "Last name",
            "username": "Username",
            "email": "Email",
            "license": "License",
            "password": "Password",
            "password2": "Confirm Password",
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords didn't match")
        return cleaned_data
