from django.shortcuts import render

data = {
    'title': 'Главная страница?',
    'values': ['text1', 'text2', 'text3'],
    'obj': {
        'a': 'qwe',
        'b': 'asd',
        'c': 'zxc'
    }
}

def index(request):
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def info(request):
    return render(request, 'main/info.html')