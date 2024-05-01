'''Forms for profile app'''
from django.forms import Form, ModelForm
from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth.models import User
from .models import *


class MyCustomLoginForm(LoginForm):
    '''Login Form'''
    def __init__(self, *args, **kwargs):
        '''Add bootstrap floating input field styling'''
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'remember':
                form_id = 'floating' + field.capitalize()
                self.fields[field].widget.attrs.update(
                    {
                        'class': 'form-control',
                        'placeholder': '',
                        'id': form_id
                    }
                    )
            else:
                form_id = field.capitalize()
                self.fields[field].widget.attrs.update({
                    'class': 'form-check-input float-end',
                    'role': 'switch',
                    'id': form_id
                })

    class Meta:
        model = User


class MyCustomSignupForm(SignupForm):
    '''Sign up form'''
    def __init__(self, *args, **kwargs):
        '''Add bootstrap floating input field styling'''
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            form_id = 'floating' + field.capitalize()
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': '',
                'id': form_id
            })

    class Meta:
        model = User
        fields = ['email', 'username']


class CustomUserChangeForm(ModelForm):
    '''User update form'''
    def __init__(self, *args, **kwargs):
        '''Add bootstrap floating input field styling'''
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            form_id = 'floating' + field.capitalize()
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': '',
                'id': form_id
            })

    password = None

    class Meta:
        model = Profile
        exclude = ['user', 'friends']


class FriendRequestForm(Form):
    '''Blank form for friend requests'''
    pass


class UpdateFriendRequestForm(ModelForm):
    '''Update friend request form'''
    readonly = ("sender", "receiver")

    def __init__(self, *args, **kwargs):
        '''Add bootstrap floating input field styling'''
        super(UpdateFriendRequestForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'status':
                form_id = 'floating' + field.capitalize()
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': '',
                    'id': form_id
                    })
                self.fields[field].required = False
            else:
                form_id = 'floating' + field.capitalize()
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': '',
                    'id': form_id
                })

        for x in self.readonly:
            self.fields[x].widget.attrs['disabled'] = True

    def clean(self):
        '''Disable readonly fields'''
        data = super(UpdateFriendRequestForm, self).clean()
        for x in self.readonly:
            data[x] = getattr(self.instance, x)
        return data

    password = None

    class Meta:
        model = FriendRequest
        fields = '__all__'


class UpdateFriendRequestSentForm(ModelForm):
    '''Form to update sent friend requests'''
    readonly = ("sender", "receiver")

    def __init__(self, *args, **kwargs):
        '''Add bootstrap floating input field styling'''
        super(UpdateFriendRequestSentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            form_id = 'floating' + field.capitalize()
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': '',
                'id': form_id
            })
            self.fields[field].required = False

        for x in self.readonly:
            self.fields[x].widget.attrs['disabled'] = True

    def clean(self):
        '''disable readonly fields'''
        data = super(UpdateFriendRequestSentForm, self).clean()
        for x in self.readonly:
            data[x] = getattr(self.instance, x)
        return data

    password = None

    class Meta:
        model = FriendRequest
        fields = ['sender', 'receiver']


class SessionInviteUpdateForm(ModelForm):
    '''Form to update session invites'''
    readonly = ["session"]

    def __init__(self, *args, **kwargs):
        '''Add bootstrap floating input field styling'''
        super(SessionInviteUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            form_id = 'floating' + field.capitalize()
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': '',
                'id': form_id
            })
            self.fields[field].required = False

            for x in self.readonly:
                self.fields[x].widget.attrs['disabled'] = True

    def clean(self):
        '''disable reasonly fields'''
        data = super(SessionInviteUpdateForm, self).clean()
        for x in self.readonly:
            data[x] = getattr(self.instance, x)
        return data

    class Meta:
        model = SessionInvite
        fields = ['session', 'status']


class SessionJoinForm(ModelForm):
    '''Form to create session join reqeust'''
    readonly = ["session"]

    def __init__(self, *args, **kwargs):
        '''Add bootstrap floating input field styling'''
        super(SessionJoinForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            form_id = 'floating' + field.capitalize()
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': '',
                'id': form_id
            })
            self.fields[field].required = False

            for x in self.readonly:
                self.fields[x].widget.attrs['disabled'] = True

    def clean(self):
        '''Disable readonly fields'''
        data = super(SessionJoinForm, self).clean()
        for x in self.readonly:
            data[x] = getattr(self.instance, x)
        return data

    class Meta:
        model = SessionInvite
        fields = ['session']
