from django import forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import News


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               help_text='Имя пользователя максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'autocomplete': 'off'}))
    password1 = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')
#        widgets = {
#            'username': forms.TextInput(attrs={'class': 'form-control'}),
#            'email': forms.EmailInput(attrs={'class': 'form-control'}),
#            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
#            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
#    }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        else:
            return title
