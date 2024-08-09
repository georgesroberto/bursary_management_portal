from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class UserTests(TestCase):
    def test_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'status': 'student',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(get_user_model().objects.filter(username='testuser').exists())
