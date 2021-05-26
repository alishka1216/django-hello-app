from django.urls import path, include
# from api_vi2 import ArticleView
from rest_framework.routers import DefaultRouter

from api_vi2.views import ArticleViewSet

app_name = 'api_vi2'


# article_urls = [
#     path('', ArticleView.as_view(), name='articles'),
#     path('<int:pk>/', ArticleView.as_view(), name='articles'),
# ]
api_router = DefaultRouter()
api_router.register('articles', ArticleViewSet)

urlpatterns = [
    path('', include(api_router.urls))
]


# urlpatterns = [
#     path('articles/', include(article_urls))
# ]