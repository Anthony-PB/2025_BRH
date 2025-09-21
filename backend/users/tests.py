from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class UserAPISuccessTests(APITestCase):
    """Test user registration and authentication - success scenarios only"""

    def test_create_user_success(self):
        """Test successful user registration with all fields"""
        url = reverse("register")
        data = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'password_confirm': 'testpass123',
            'first_name': 'Test',
            'last_name': 'User',
            'display_name': 'TestUser'
        }

        response = self.client.post(url, data, format='json')

        # Check if user was created successfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertIn('user', response.data)
        self.assertEqual(response.data['user']['email'], 'test@example.com')
        self.assertEqual(response.data['user']['display_name'], 'TestUser')
        self.assertNotIn('password_hash', response.data)
        self.assertNotIn('password_hash', response.data)

        # Verify user exists in database
        self.assertTrue(User.objects.filter(email='test@example.com').exists())

    def test_create_user_minimal_fields(self):
        """Test successful user registration with minimal required fields"""
        url = reverse("register")
        data = {
            'email': 'minimal@example.com',
            'password': 'securepass456',
            'password_confirm': 'securepass456'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertEqual(response.data['user']['email'], 'minimal@example.com')
        self.assertNotIn('password_hash', response.data)
        self.assertNotIn('password_hash', response.data)
        # Verify user was created
        user = User.objects.get(email='minimal@example.com')
        self.assertEqual(user.email, 'minimal@example.com')

    def test_create_user_with_long_password(self):
        """Test successful registration with a longer password"""
        url = reverse("register")
        data = {
            'email': 'longpass@example.com',
            'password': 'thisisaverylongandstrongpassword123',
            'password_confirm': 'thisisaverylongandstrongpassword123',
            'first_name': 'Long',
            'last_name': 'Password',
            'display_name': 'LongPassUser'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertNotIn('password_hash', response.data)

        self.assertTrue(User.objects.filter(
            email='longpass@example.com').exists())

    def test_create_multiple_users(self):
        """Test creating multiple users successfully"""
        url = reverse("register")

        users_data = [
            {
                'email': 'user1@example.com',
                'password': 'pass123456',
                'password_confirm': 'pass123456',
                'display_name': 'User One'
            },
            {
                'email': 'user2@example.com',
                'password': 'pass789012',
                'password_confirm': 'pass789012',
                'display_name': 'User Two'
            }
        ]

        for user_data in users_data:
            response = self.client.post(url, user_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertIn('token', response.data)
            self.assertNotIn('password_hash', response.data)

        # Verify both users exist
        self.assertEqual(User.objects.count(), 2)
        self.assertTrue(User.objects.filter(
            email='user1@example.com').exists())
        self.assertTrue(User.objects.filter(
            email='user2@example.com').exists())

    def test_token_is_unique_per_user(self):
        """Test that each user gets a unique authentication token"""
        url = reverse("register")

        # Create first user
        response1 = self.client.post(url, {
            'email': 'token1@example.com',
            'password': 'testpass123',
            'password_confirm': 'testpass123'
        }, format='json')

        # Create second user
        response2 = self.client.post(url, {
            'email': 'token2@example.com',
            'password': 'testpass123',
            'password_confirm': 'testpass123'
        }, format='json')

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)

        token1 = response1.data['token']
        token2 = response2.data['token']

        # Tokens should be different
        self.assertNotEqual(token1, token2)

        # Both tokens should exist and be valid strings
        self.assertTrue(isinstance(token1, str))
        self.assertTrue(isinstance(token2, str))
        self.assertTrue(len(token1) > 10)  # Reasonable token length
        self.assertTrue(len(token2) > 10)

    def test_get_profile(self):
        """Test getting authenticated user's profile"""
        data = {
            'email': 'minimal@example.com',
            'password': 'securepass456',
            'password_confirm': 'securepass456'
        }

        response = self.client.post(reverse('register'), data, format='json')
        self.client.force_authenticate(
            user=User.objects.get_by_natural_key(response.data['user']['email']))
        url = reverse("profile-manager")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'minimal@example.com')
        self.assertEqual(response.data['display_name'], '')

    def test_delete_profile_success(self):
        """Test successful profile deletion"""
        data = {
            'email': 'minimal@example.com',
            'password': 'securepass456',
            'password_confirm': 'securepass456'
        }

        response = self.client.post(reverse('register'), data, format='json')
        self.client.force_authenticate(
            user=User.objects.get_by_natural_key(response.data['user']['email']))
        user_id = response.data['user']['id']
        url = reverse("profile-manager")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data['message'],
                         'User deleted successfully.')
        # Verify user was deleted
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=user_id)

    def test_unauthorized_access(self):
        """Test profile access without authentication"""
        self.client.logout()  # Remove authentication
        url = reverse("profile-manager")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
