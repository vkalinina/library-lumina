from django.test import TestCase

from catalog.forms import AuthorCreationForm
from catalog.models import Author


class FormsTests(TestCase):
    def test_author_creation_form_with_pseudonym_first_name_last_name_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "passQ123sdgd",
            "password2": "passQ123sdgd",
            "first_name": "Test first_name",
            "last_name": "Test last_name",
            "pseudonym": "Test pseudonym",
        }
        form = AuthorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
