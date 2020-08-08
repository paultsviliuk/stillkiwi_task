import pytest
from model_mommy import mommy
from django.test import TestCase
from redirects_analyzer.models import RedirectData


pytestmark = pytest.mark.django_db


class RedirectDataTestMommy(TestCase):

    def test_fredirect_data_creation_mommy(self):
        new_redirect_record = mommy.make(RedirectData)
        self.assertTrue(isinstance(new_redirect_record, RedirectData))
        self.assertEqual(new_redirect_record.__str__(), new_redirect_record.redirect_url)
