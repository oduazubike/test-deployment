from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.


class FirstTest(generics.GenericAPIView):

    def get(self, request):

        data = {"Message": "I am Running LIVE!!!!"}
        return Response(data, status=status.HTTP_200_OK)



