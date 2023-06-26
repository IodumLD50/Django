from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse('<h1>Для просмотра задания "/news/test", "/news/test2"<h1>')
def test_1(request):
    return HttpResponse('<h1>Шаблон MVC, контроллеры и маршруты.</h1>')

def test_2(request):
    return HttpResponse('<h2>Задание выполнено!</h2>')
