from django.forms import Form
from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Profile

class MyCustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'remember':
                form_id = 'floating' + field.capitalize()
                self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': '', 'id': form_id})
            else:
                form_id = field.capitalize()
                self.fields[field].widget.attrs.update({'class': 'form-check-input float-end', 'role': 'switch','id': form_id})
    
    class Meta:
        model = User

    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)
    

class MyCustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            form_id = 'floating' + field.capitalize()
            self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': '', 'id': form_id})
    
    class Meta:
        model = User
        fields = ['email', 'username']

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user

class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            form_id = 'floating' + field.capitalize()
            self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': '', 'id': form_id})

    password = None
    class Meta:
        model = Profile
        exclude = ['user', 'friends']

class FriendRequestForm(Form):
    pass