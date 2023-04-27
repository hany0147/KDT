from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    birthday = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date'},
        ),
        label='생년월일',
    )
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username','email','first_name','last_name','password1','password2','birthday')


class CustomUserChangeForm(UserChangeForm):
    birthday = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date'},
        ),
        label='생년월일',
    )
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'birthday',)
