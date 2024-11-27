from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from Core.models.User import User
from datetime import date

from Core.models.BIG_CALENDAR import BIG_CALENDAR


class BIG_CALENDAR_Api_View_Test(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.admin_user = User.objects.create_superuser(
            username='admin', password='password', email='admin@example.com'
        )

    def authenticate(self):
        refresh = RefreshToken.for_user(self.admin_user)
        access_token = str(refresh.access_token)

        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {access_token}')

    def test_create_calendar(self):
        self.authenticate()

        url = '/api/sys/big_calendars/'

        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(BIG_CALENDAR.objects.all().count(), 365)

        first_calendar_entry = BIG_CALENDAR.objects.first().day
        self.assertEqual(first_calendar_entry, date(2025, 1, 1))
