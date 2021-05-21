
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json
import math
from article.models import Article

@ensure_csrf_cookie
def get_csrf_token_view(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps({"token":"ok"}))
    return HttpResponse(status=405)



def add(request):
    if request.body:
        try:
            response_context = json.loads(request.body)
            answer = int(response_context['A']) + int(response_context['B'])
            response_body = {
                'answer' : answer
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
        except:
            response_body = {
                'error': "error"
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
            response.status_code = 400
        return response


def subtract(request):
    if request.body:
        try:
            response_context = json.loads(request.body)
            answer = int(response_context['A']) - int(response_context['B'])
            response_body = {
                'answer' : int(answer)
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
        except:
            response_body = {
                'error': "error"
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
            response.status_code = 400
        return response


def multiply(request):
    if request.body:
        try:
            response_context = json.loads(request.body)
            answer = int(response_context['A']) * int(response_context['B'])
            response_body = {
                'answer' : answer
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
        except:
            response_body = {
                'error': "error"
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
            response.status_code = 400
        return response


def devide(request):
    if request.body:
        try:
            response_context = json.loads(request.body)
            answer = int(response_context['A']) / int(response_context['B'])
            response_body = {
                'answer' : answer
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
        except:
            response_body = {
                'error': "error"
            }
            response = HttpResponse(json.dumps(response_body))
            response['content-type'] = 'application/json'
            response.status_code = 400
        return response