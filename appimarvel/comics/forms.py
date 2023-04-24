from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserREgisterForm(UserCreationForm):
    username=forms.CharField(label='Nombre')
    identificacion=forms.CharField()
    email=forms.EmailField(label='Correo Eletronico')
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput)
    
    class  Meta:
        model=User
        fields=['username', 'identificacion','email', 'password1','password2']
        help_texts={k:"" for k in fields}