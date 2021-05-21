from django.urls import path, include
from api_vi2 import ArticleView

app_name = 'api_vi2'


article_urls = [
    path('', ArticleView.as_view(), name='articles'),
    path('<int:pk>/', ArticleView.as_view(), name='articles'),
]

urlpatterns = [
    path('articles/', include(article_urls))
]