from django.forms import Form, ModelForm
from .models import Game, Group ,Session, Fixture

class GroupCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GroupCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields: 
            self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': '', 'id': 'floatingEmail'})

    class Meta:
        model = Group
        exclude = ['host']