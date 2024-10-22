from django import forms
from rent_app.models import CAR
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


class CarForm(forms.ModelForm):
    class Meta:
        model = CAR
        fields = '__all__'  # Include all fields except owner

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user:
            self.instance.owner = self.user


class SignUpForm(UserCreationForm): 
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
