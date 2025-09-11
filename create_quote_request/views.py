from rest_framework.response import Response
from rest_framework.views import APIView

from create_quote_request.serializers import QuoteRequestSerializer


class QuoteRequestApiView(APIView):

    def post(self, request):
        serializer = QuoteRequestSerializer(data=request.data)

        if serializer.is_valid():
            return Response(request.data, status=201)
        
        return Response(serializer.errors, status=400)
