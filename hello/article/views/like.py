from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from article.models import Article, ArticleUser, Comment, CommentUser


class ArticleLike(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            ArticleUser.objects.get(article=article, user=user)

        except ArticleUser.DoesNotExist:
            ArticleUser.objects.create(article=article, user=user)

        return redirect('article:view', article.pk)


class ArticleUnlike(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            like = ArticleUser.objects.get(article=article, user=user)
            like.delete()
        except ArticleUser.DoesNotExist:
            pass
        return redirect('article:view', article.pk)


class CommentLike(View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            CommentUser.objects.get(comment=comment, user=user)
        except CommentUser.DoesNotExist:
            CommentUser.objects.create(comment=comment, user=user)

        return redirect('article:view', comment.article.pk)


class CommentUnlike(View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            like = CommentUser.objects.get(comment=comment, user=user)
            like.delete()
        except CommentUser.DoesNotExist:
            pass

        return redirect('article:view', comment.article.pk)