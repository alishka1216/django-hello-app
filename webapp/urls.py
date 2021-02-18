from django.urls import path

from .views import index_view, home_view


urlpatterns = [
    path('hello/', index_view),
    path('', home_view),
]