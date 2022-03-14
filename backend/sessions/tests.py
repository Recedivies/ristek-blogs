from rest_framework.test import APIClient, APITestCase


class UserAuthentication(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
