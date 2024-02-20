from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from .models import Concert,Category
from .serializers import ConcertSerializer
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class ConcertAPIView(APIView):
    def get(self, request):
        lst = Concert.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Concert.objects.create(
            title = request.data['title'],
            content = request.date['content'],
            cat_id = request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})


# class ConcertAPIView(APIView):
#     queryset = Concert.objects.all()
#     serializer_class = ConcertSerializer

class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer