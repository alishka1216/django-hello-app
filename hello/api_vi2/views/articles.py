import json

from django.db.migrations import serializer
from django.http import JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from api_vi2 import serializers
from article.models import Article

from api_vi2.serializers import ArticleSerializer, article

#for viewSet!

from rest_framework.viewsets import ModelViewSet


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()













class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


    def get(self, request,  *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            if pk:
                return Response(ArticleSerializer(Article.objects.get(pk=pk)).data)
        except Article.DoesNotExist as e:
            return Response({'error': "error"}, status=status.HTTP_400_BAD_REQUEST)
        articles = Article.objects.all()
        a = ArticleSerializer(articles, many=True)
        print(a)
        print()
        print(a.data)
        response_data = ArticleSerializer(articles, many=True).data
        return Response(data=response_data)


    def post(self, request, *args, **kwargs):
        article_data = request.data
        serializer = ArticleSerializer(data={**article_data, 'qwe':''})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        article_data = request.data
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article, data=article_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
            article.delete()
        except Article.DoesNotExist as e:
            return Response({'error': "error"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"pk": pk})