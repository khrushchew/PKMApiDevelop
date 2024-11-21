from rest_framework.test import APITestCase
from rest_framework import status

from Core.models.User import User
from datetime import date

from BIG_CALENDAR_API.models.BIG_CALENDAR import BIG_CALENDAR

class BIG_CALENDAR_Api_View_Test(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.admin_user = User.objects.create_superuser(
            username='admin', password='password', email='admin@example.com'
        )

    def test_create_calendar(self):
        self.client.login(username='admin', password='password')
        
        url = '/api/sys/big_calendars/' 
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(BIG_CALENDAR.objects.all().count(), 365)
        
        first_calendar_entry = BIG_CALENDAR.objects.first()
        self.assertEqual(first_calendar_entry.date, date(2025, 1, 1))

