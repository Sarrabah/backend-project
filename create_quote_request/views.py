from rest_framework.response import Response
from rest_framework.views import APIView

from create_quote_request.serializers import QuoteRequestSerializer
from create_quote_request.services import create_quote_request


class QuoteRequestApiView(APIView):

    def post(self, request):
        serializer = QuoteRequestSerializer(data=request.data)

        if serializer.is_valid():
            try:
                new_quote_request = create_quote_request(
                    request, serializer.validated_data
                )
                created_data = QuoteRequestSerializer(new_quote_request).data
                return Response(created_data, status=201)
            except Exception as e:
                return Response(
                    {"error": f"An unexpected error occurred: {str(e)}"}, status=500
                )

        return Response(serializer.errors, status=400)
