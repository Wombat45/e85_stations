from django.test import TestCase, Client
from django.urls import reverse
from .forms import StationForm
from .views import index

class StationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse(index)

    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_POST_valid_data(self):
        form = StationForm(data={
            'zip_code': '19128',
            'miles': '55'
        })

        self.assertTrue(form.is_valid())

    def test_index_POST_no_data(self):
        form = StationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)