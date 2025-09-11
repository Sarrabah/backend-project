from rest_framework.response import Response
from rest_framework.views import APIView

from create_quote_request.serializers import QuoteRequestSerializer
from create_quote_request.services import create_quote_request


class QuoteRequestApiView(APIView):

    def post(self, request):
        serializer = QuoteRequestSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        try:
            valid_data = serializer.validated_data
            new_quote_request = create_quote_request(request, valid_data)
            return self._successful_response_created(new_quote_request)
        except Exception as e:
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"}, status=500
            )

    def _successful_response_created(self, new_quote_request):
        """Retourne la réponse HTTP 201 avec les données sérialisées."""
        created_data = QuoteRequestSerializer(new_quote_request).data
        return Response(created_data, status=201)
