from django.forms import Form, ModelForm
from .models import Game, Group ,Session, Fixture

class GroupCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GroupCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'private':
                form_id = 'floating' + field.capitalize()
                self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': '', 'id': form_id})
            else:
                form_id = field.capitalize()
                self.fields[field].widget.attrs.update({'class': 'form-check-input float-end', 'role': 'switch','id': form_id})

    class Meta:
        model = Group
        exclude = ['host']

class SessionCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SessionCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields: 
            self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': '', 'id': 'floatingEmail'})

    class Meta:
        model = Session
        exclude = ['status', 'joinable', 'admin', 'players', 'group']

class SessionUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SessionUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields: 
            self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': '', 'id': 'floatingEmail'})

    class Meta:
        model = Session
        exclude = ['status', 'joinable', 'players', 'group']