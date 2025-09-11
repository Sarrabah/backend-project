from rest_framework import serializers

from create_quote_request.models import QuoteRequest


class QuoteRequestSerializer(serializers.ModelSerializer):
    STATUS_CHOICES = ["Created", "InProgress", "Completed"]
    status = serializers.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = QuoteRequest
        fields = ["id", "title", "description", "status"]

    def validate_title(self, value):
        if len(value) == 0:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        if len(value) == 0:
            raise serializers.ValidationError("Description cannot be empty.")
        return value
