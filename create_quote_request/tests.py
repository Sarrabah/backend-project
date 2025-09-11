from unittest.mock import MagicMock

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class QuoteRequestAPITestCase(TestCase):

    def setUp(self):
        # Créer un client API
        self.client = APIClient()
        # Simuler un utilisateur
        self.archi = MagicMock()
        self.archi.id = 1
        self.archi.username = "philippe"

        # Authentifier le client avec l'objet mock
        self.client.force_authenticate(user=self.archi)
        self.url = reverse("add-new-quote-request")

    def test_create_quote_request_api_success_status(self):
        payload = {
            "title": "First quote request",
            "description": "First quote request description",
            "status": "Created",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
