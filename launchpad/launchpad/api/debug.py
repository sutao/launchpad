from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class Ping(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response({'message': 'Pong'})
