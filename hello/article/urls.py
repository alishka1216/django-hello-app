from django.urls import path
from article.views.like import (
    ArticleLike,
    ArticleUnlike,
    CommentLike,
    CommentUnlike,

)
from article.views import (
    IndexView,
    ArticleView,
    CreateArticleView,
    ArticleUpdateView,
    ArticleCommentCreate,
    ArticleDeleteView,
    getIndex
)


app_name = 'article'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('add/', CreateArticleView.as_view(), name='add'),
    path('<int:pk>/', ArticleView.as_view(), name='view'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete'),
    path('<int:pk>/comments/add/', ArticleCommentCreate.as_view(), name='comment-create'),
    path('<int:pk>/Articlelike/', ArticleLike.as_view(), name='article_like'),
    path('<int:pk>/Articleunlike/', ArticleUnlike.as_view(), name='article_unlike'),
    path('<int:pk>/Commentlike/', CommentLike.as_view(), name='comment_like'),
    path('<int:pk>/Commentunlike/', CommentUnlike.as_view(), name='comment_unlike'),
    path('index/', getIndex, name='index_count')
]
