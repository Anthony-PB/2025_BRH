from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Source


class SourceTests(APITestCase):

    def test_create_multiple_sources(self):
        """Test creating multiple sources successfully"""
        url = reverse("source-create")  # matches your urls.py name

        sources_data = [
            {
                'name': 'TechCrunch',
                'base_url': 'https://techcrunch.com',
                'feed_url': 'https://techcrunch.com/feed',
                'is_rss': True,
                'category': 'Technology',
                'is_active': True
            },
            {
                'name': 'BBC News',
                'base_url': 'https://bbc.com',
                'feed_url': 'https://bbc.com/news/rss.xml',
                'is_rss': True,
                'category': 'News',
                'is_active': True
            }
        ]

        for source_data in sources_data:
            response = self.client.post(url, source_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertIn('source', response.data)
            self.assertEqual(
                response.data['source']['name'], source_data['name'])

        # Verify both sources exist in the database
        self.assertEqual(Source.objects.count(), 2)
        self.assertTrue(Source.objects.filter(name='TechCrunch').exists())
        self.assertTrue(Source.objects.filter(name='BBC News').exists())

    def test_list_active_sources(self):
        """Test listing only active sources"""
        url = reverse("source-create")  # same endpoint for list (GET)

        # Create sources manually
        Source.objects.create(name='Active Source',
                              base_url='https://active.com', is_active=True)
        Source.objects.create(name='Inactive Source',
                              base_url='https://inactive.com', is_active=False)

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['sources'][0]['name'], 'Active Source')
