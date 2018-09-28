from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from .models import Weight


username = 'user1'
password = 'password1'


class ModelsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        ''' Run once to set up non-modified data for all class methods.
        '''
        pass

    def setUp(self):
        ''' Run once for every test method to setup clean data.
        '''

        # Create users
        u1 = User.objects.create_user(username=username, password=password)
        self.assertIsNotNone(u1)

        # Create weights
        w1 = Weight.objects.create(date=timezone.now(), weight=200, user=u1)
        self.assertIsNotNone(w1)

    def test_user(self):
        self.assertEqual(User.objects.count(), 1)

        # Not logged in
        response = self.client.get(reverse('weights'))
        self.assertEqual(response.status_code, 302)

        # Logged in
        login = self.client.login(username=username, password=password)
        response = self.client.get(reverse('weights'))
        self.assertEqual(response.status_code, 200)

    def test_weight_count(self):
        self.assertEqual(Weight.objects.count(), 1)

    def test_weight_valid(self):
        u1 = User.objects.get(pk=1)
        w1 = Weight.objects.get(user_id=u1.id)
        self.assertTrue(w1.weight > 0)
        self.assertTrue(w1.body_fat is None
                        or w1.body_fat >= 0 and w1.body_fat <= 1)
