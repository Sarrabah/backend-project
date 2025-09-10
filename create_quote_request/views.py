from rest_framework.response import Response
from rest_framework.views import APIView


class QuoteRequestApiView(APIView):

    def post(self, request):
        return Response(status=201)
