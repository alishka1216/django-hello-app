from django.urls import path, include
from api_vi.views import add, subtract,get_csrf_token_view, multiply, devide

app_name = 'api_vi'


urlpatterns = [
    path('get_csrf_token_view/', get_csrf_token_view, name='get_csrf_token_view'),
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('devide/', devide, name='devide')
]