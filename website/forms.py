from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordResetForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from fama import settings
from website.models import Fama as FamaModel, Reporter, Ticket


class FamaForm(forms.ModelForm):
    class Meta:
        model = FamaModel
        fields = ['title', 'desc', 'place']
        widget = {
            'author': forms.HiddenInput(),
            'pub_date': forms.HiddenInput(),
            'last_edited': forms.HiddenInput()
        }


#for now i am using for registration
class UserForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput,
        error_messages = {'required': "your username must not leave it empty.", 'invalid': 'invalid username.'},
        max_length=30)
    email = forms.EmailField(
        widget=forms.EmailInput,
        error_messages = {'required': "your email must not leave it empty", 'invalid': 'invalid email.'}
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        error_messages = {'required': "your password must not leave it empty.", 'invalid': 'invalid password.'},
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        error_messages = {'required': "your password must not leave it empty.", 'invalid': 'invalid password.'}
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise forms.ValidationError('your password must not leave it empty.')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("password mismatch.")
        return password2

    def clean(self):
        email =  self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not email:
            raise forms.ValidationError('your email must not leave it empty')

        if not password1 or not password2:
            raise forms.ValidationError('your password must not leave it empty.')


    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user


class ReporterForm(forms.ModelForm):
    class Meta:
        model = Reporter
        fields = []


class MyLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput,
        error_messages = {'required': "your username must not leave it empty.", 'invalid': 'invalid username.'},
        max_length=30)
    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages = {'required': "your password must not leave it empty.", 'invalid': 'invalid password.'})

    error_messages = {
        'invalid_login': "you may have entered incorrect your username and your password."
    }

class MyPasswordReset(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput,
        error_messages = {'required': "your email must not leave it empty", 'invalid': 'invalid email.'}
    )

    def clean(self):
        email =  self.cleaned_data.get('email')

        if not email:
            raise forms.ValidationError('your email must not leave it empty')

        if not User.objects.filter(email=email):
            raise forms.ValidationError("any user didn't sign up with this email.")


class ChangeEmailForm(forms.Form):
    old_email = forms.EmailField(
        widget=forms.EmailInput,
        error_messages = {'required': "your old email must not leave it empty.", 'invalid': 'invalid email.'}
    )

    new_email = forms.EmailField(
        widget=forms.EmailInput,
        error_messages = {'required': "your new email must not leave it empty.", 'invalid': 'invalid email.'}
    )

    def clean(self):
        old_email =  self.cleaned_data.get('old_email')
        new_email =  self.cleaned_data.get('new_email')

        if not old_email:
            raise forms.ValidationError("your new email must not leave it empty.")
        elif not User.objects.filter(email=old_email):
            raise forms.ValidationError("wrong old email.")

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages = {
            'required': "your old password must not leave it empty.",
            'invalid': 'invalid old password.'})

    new_password1 = forms.CharField(
        widget=forms.PasswordInput,
        error_messages = {'required': "your new password must not leave it empty.", 'invalid': 'invalid new password.'})

    new_password2 = forms.CharField(
        widget=forms.PasswordInput,
        error_messages = {'required': "your new password must not leave it empty.", 'invalid': 'invalid new password.'})

    error_messages = {'password_incorrect': "your old password was entered incorrectly."}


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['messagge']

from django.core.files.images import get_image_dimensions
import StringIO
from PIL import Image


class ChangeProfilePictureForm(forms.Form):
    profile_picture = forms.ImageField()


    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get('profile_picture')


        if profile_picture:
            if profile_picture._size > 2 * 1024 * 1024:
                raise ValidationError("image file too large. max 2mb.")




