from django.forms import ModelForm
from onekey.services.models import Author, Book
from onekey.debug import debug


class AuthorForm(ModelForm):

    def __init__(self, data=None, files=None, auto_id=None, prefix=None, initial=None,
            error_class=None, label_suffix=':', empty_permitted=False, instance=None) :
        """ Constructor for AuthorForm Class """
        ModelForm.__init__(self, data=None, files=None, auto_id=None, prefix=None, initial=None,
            error_class=None, label_suffix=':', empty_permitted=False, instance=None)
        self.base_fields['title'].choices = [(0,'zero'),(1,'one')]

    def clean(self):
        """ Validation form """
        debug()

    class Meta:
        model = Author


class BookForm(ModelForm):
    class Meta:
        model = Book
