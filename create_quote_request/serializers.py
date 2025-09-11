from rest_framework import serializers

from create_quote_request.models import QuoteRequest


class QuoteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteRequest
        fields = ["id", "title", "description", "status"]
