from django.forms import Form, ModelForm
from .models import Game, Group ,Session, Fixture

class GroupCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GroupCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            print(field)
            if field != 'private':
                form_id = 'floating' + field.capitalize()
                self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': '', 'id': form_id})
            else:
                form_id = field.capitalize()
                self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': '', 'id': form_id})

    class Meta:
        model = Group
        exclude = ['host']