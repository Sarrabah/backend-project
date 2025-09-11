from unittest.mock import MagicMock, patch

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

        self.url = reverse("add-new-quote-request")

    @patch("create_quote_request.views.create_quote_request")
    def test_create_quote_request_api_success(self, mock_create):
        mock_obj = MagicMock()
        mock_obj.title = "First quote request"
        mock_obj.description = "First quote request description"
        mock_obj.status = "Created"
        mock_create.return_value = mock_obj

        payload = {
            "title": "First quote request",
            "description": "First quote request description",
            "status": "Created",
        }
        response = self.client.post(self.url, payload, format="json")

        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data["title"], payload["title"])
        self.assertEqual(data["description"], payload["description"])
        self.assertEqual(data["status"], payload["status"])

    def test_create_quote_request_api_missing_field(self):
        payload = {
            "title": "First quote request",
            "description": "First quote request description",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch(
        "create_quote_request.views.create_quote_request",
        side_effect=Exception("DB failure"),
    )
    def test_create_quote_request_unexpected_error_returns_500(self, mock_create):
        payload = {
            "title": "First quote request",
            "description": "First quote request description",
            "status": "Created",
        }
        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
