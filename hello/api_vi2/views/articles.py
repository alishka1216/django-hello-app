import json

from django.http import JsonResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from api_vi2 import serializers
from article.models import Article

from api_vi2.serializers import ArticleSerializer, article


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        response_data = ArticleSerializer(articles, many=True).data
        print(response_data)
        return Response(data=response_data)


    def post(self, request, *args, **kwargs):
        article_data = request.data
        serializer = ArticleSerializer(data={**article_data, 'qwe':''})
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        return JsonResponse({'id': article.id})
