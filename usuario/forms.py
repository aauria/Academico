from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm
from django import forms



class RegistroForms(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_superuser',
            'groups'

        ]
        labels={
            'username':'Nombre de Usuario',
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'Correo Electronico',
            'is_staff':'Usuario_Normal',
            'is_superuser':'Super_Usuario',
            'groups':'Grupo'

        }
        widgets={
            'groups':forms.SelectMultiple(attrs={'class': 'form-control'}),
        }



    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            for grupo in self.cleaned_data.get("groups"):
                my_group = Group.objects.get(name=grupo)
                my_group.user_set.add(user)
        return user



class GroupForms(forms.ModelForm):
    class Meta:
        model=Group
        fields=[
            'name',
            'permissions',

        ]
        labels={
            'name':'Nombre del Grupo ',
            'permissions':'Permisos ',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'permissions': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }

