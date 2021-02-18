from lib2to3.fixes.fix_input import context

from django.shortcuts import render


# Create your views here.
def index_view(request):
    return render(request, 'index.html')


def home_view(request):
    print(request.GET.getlist('title'))
    return render(request, 'home.html')


def page_view(request):
    return render(request, 'page.html')


def article_create_view(request):
    if request.method == "GET":
        return render(request, 'article_create.html')
    elif request.method == "POST":
        user = {'name': 'mei', 'emal': 'mei1216@mail.ru', "age":21}
        context = {
            'title': request.POST.get('title'),
            'content': request.POST.get('content'),
            'author': request.POST.get('author'),
            'user': user
        }
        return render(request, 'article_view.html', context)
