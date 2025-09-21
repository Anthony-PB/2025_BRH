from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from .views import Source
import dateparser
from .models import Source
from django.contrib.auth import get_user_model

User = get_user_model()


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

    def test_list_when_no_active_sources(self):
        """Test listing sources when none are active"""
        url = reverse("source-create")  # use local variable
        Source.objects.update(is_active=False)
        response = self.client.get(url, format='json')  # use url, not self.url
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)
        self.assertEqual(response.data['sources'], [])


class UserFollowTests(APITestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(
            username="testuser@example.com",
            email="testuser@example.com",
            password="password123"
        )

        # Create a test source
        self.source = Source.objects.create(
            name="Test Source",
            base_url="https://example.com",
            is_active=True
        )

        # Authenticate client
        self.client.force_authenticate(user=self.user)

    def test_follow_source(self):
        url = reverse('follow-source', args=[str(self.source.id)])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(str(self.source.id), self.user.followed_source_ids)

    def test_unfollow_source(self):
        # First follow it
        self.user.follow_source(self.source.id)

        url = reverse('unfollow-source', args=[str(self.source.id)])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(str(self.source.id), self.user.followed_source_ids)


class LoadFromSourceTests(APITestCase):
    def test_load_small_rss(self):
        item = Source.objects.create(**{'name': 'ExampleRSS',
                                        'url': 'https://files.catbox.moe/ppfxwh.xml',
                                        'category': 'Extra',
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
        self.assertEqual(l[0]['date_published'], dateparser.parse(
            "Thu, 19 Sep 2025 10:00:00 EDT"))
        self.assertTrue(all(l[i]['date_published'] >= l[i + 1]
                        ['date_published'] for i in range(len(l) - 1)))
