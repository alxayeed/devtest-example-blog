from django.forms import ModelForm, ValidationError
from django.contrib.auth.forms import UserCreationForm
from authentication.models import User


class RegisterForm(UserCreationForm):
    '''
    Form for user registration
    '''

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'password1', 'password2']
