import logging

from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from create_quote_request.domaine.services import create_quote_request
from create_quote_request.infrastructure.serializers import QuoteRequestSerializer

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class QuoteRequestApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Create a new quote request",
        request_body=QuoteRequestSerializer,
        responses={
            201: QuoteRequestSerializer,
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal error",
        },
    )
    def post(self, request):
        serializer = QuoteRequestSerializer(data=request.data)

        if not serializer.is_valid():
            logger.error(f"Validation error: {serializer.errors}")
            return Response(serializer.errors, status=400)

        try:
            valid_data = serializer.validated_data
            new_quote_request = create_quote_request(request, valid_data)
            response = self._successful_response_created(new_quote_request)
            logger.info(
                f"QuoteRequest created with ID: {new_quote_request.id} by user: {request.user.id}"
            )
            return response
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"}, status=500
            )

    def _successful_response_created(self, new_quote_request):
        created_data = QuoteRequestSerializer(new_quote_request).data
        return Response(created_data, status=201)
