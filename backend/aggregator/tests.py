from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from .views import Source
import dateparser

# Create your tests here.
class LoadFromSourceTests(APITestCase):
    def test_load_small_rss(self):
        item = Source.objects.create(**{'name': 'ExampleRSS', 
                               'url': 'https://files.catbox.moe/ppfxwh.xml', 
                               'category':'Extra', 
                               'is_rss': True})
        self.assertTrue(Source.objects.filter(name="ExampleRSS").exists())
        url = reverse("get-from-source", args=(item.id,), query={'count': 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 2)

        l = response.data['results']
        self.assertEqual(l[0]['title'], 'First Test Item')
        self.assertEqual(l[0]['link'], 'http://www.example.com/item1')
        self.assertEqual(l[0]['date_published'], dateparser.parse("Thu, 19 Sep 2025 10:00:00 EDT"))
        self.assertTrue(all(l[i]['date_published'] >= l[i + 1]['date_published'] for i in range(len(l) - 1)))

