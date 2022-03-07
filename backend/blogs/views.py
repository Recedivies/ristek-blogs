from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class BlogList(APIView):
    def get(self, request):
        text = request.query_params.get("text", "")
        return Response({"text": text.upper()}, status=status.HTTP_200_OK)
