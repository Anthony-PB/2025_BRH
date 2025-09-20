from django.test import TestCase
from unittest.mock import patch, MagicMock
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.hashers import make_password # <-- Import Django's hashing function


class UserAPITests(APITestCase):
    """
    Test suite for the User API endpoints.
    """
    def setUp(self):
        """This method is run before each test."""
        self.client = APIClient()

    # --- Test 1: Listing articles (GET) ---

    @patch('core.db_utils.create_user')
    def test_create_user_success(self, mock_create_user):
        """
        RED: Write a failing test for POST /users/register/.
        It should return a created user
        """
        # Arrange: Configure the mock to return some fake data
        password = "IMcool124"
        mock_create_user.return_value = {'_id': '1', 
                                              'email': 'augustiscool@gmail.com', 
                                              'sources':[],
                                              'password_hash': 'ahsdw248iffdf2@', 
                                              'liked_posts':[]}

        payload = {"email":"augustiscool@gmail.com", "password": password, "confirm_password": password}
        # Act: Make the API request
        response = self.client.post(reverse('register-user'), data=payload, format='json')

        # Assert: Check the results
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['_id'], '1')
        self.assertEqual(response.data['email'], 'augustiscool@gmail.com')
        self.assertNotIn('password_hash', response.data)
        mock_create_user.assert_called_once()


    # # --- Test 2: Creating an article (POST) - Happy Path ---

    # @patch('core.db_utils.create_article')
    # def test_create_article_success(self, mock_create_article):
    #     """
    #     RED: Test POST /api/articles/ with valid data and authentication.
    #     """
    #     # Arrange: Set up the mock and the data payload
    #     mock_create_article.return_value = 'new_article_id_123'
    #     valid_payload = {
    #         'title': 'A Brand New Article',
    #         'url': 'http://example.com/new',
    #         'author_email': 'author@example.com'
    #     }

    #     # Act: Force authenticate a user and make the POST request
    #     self.client.force_authenticate(user=DUMMY_USER)
    #     response = self.client.post(
    #         self.list_create_url, 
    #         data=valid_payload, 
    #         format='json'
    #     )

    #     # Assert
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     mock_create_article.assert_called_once_with(valid_payload)


    # # --- Test 3: Creating an article - Sad Path (Invalid Data) ---

    # def test_create_article_invalid_data(self):
    #     """
    #     RED: Test POST /api/articles/ with invalid data.
    #     It should return a 400 Bad Request error.
    #     """
    #     # Arrange: Payload is missing the required 'url' field
    #     invalid_payload = {'title': 'Missing URL'}

    #     # Act
    #     self.client.force_authenticate(user=DUMMY_USER)
    #     response = self.client.post(
    #         self.list_create_url, 
    #         data=invalid_payload, 
    #         format='json'
    #     )

    #     # Assert
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertIn('url', response.data) # Check that the error message mentions the 'url' field


    # # --- Test 4: Creating an article - Sad Path (Unauthenticated) ---

    # def test_create_article_unauthenticated(self):
    #     """
    #     RED: Test POST /api/articles/ without authentication.
    #     """
    #     # Arrange
    #     payload = {'title': 'A Title', 'url': 'http://a.com'}

    #     # Act: Note that we DO NOT call force_authenticate
    #     response = self.client.post(self.list_create_url, data=payload, format='json')

    #     # Assert: DRF should return 401 Unauthorized or 403 Forbidden
    #     # depending on your default permission settings.
    #     self.assertIn(
    #         response.status_code, 
    #         [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN]
    #     )