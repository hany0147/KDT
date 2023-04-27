from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = UsernameField(
         label='ID', 
         label_suffix='', 
         widget=forms.TextInput(
                attrs={
                    'class': 'form-control custom-signup-form-field', 
                }
            )
        )
    email = forms.EmailField(
        label='이메일',
        label_suffix='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control custom-signup-form-field'}))
    password1 = forms.CharField(
        label='비밀번호', 
        label_suffix='', 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control custom-signup-form-field'}))
    password2 = forms.CharField(
        label='비밀번호 확인', 
        label_suffix='', 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control custom-signup-form-field'}))
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'email',
        )
    
    email = forms.EmailField(label='이메일', label_suffix='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'style': 'width: 250px;'}))
    # password = None


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='',
        widget=forms.TextInput(
            attrs={
                    'class': 'form-control',
                    'autofocus': True,
                    'placeholder':"username",
                    'style': 'width: 200px',
                }
            )
        )
    password = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                    'class': 'form-control',
                    'autocomplete': 'current-password',
                    'placeholder': "password",
                    'style': 'width: 200px',
                }
            ),
        )

