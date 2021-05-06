from random import sample

from django.shortcuts import render, redirect
import json
# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.urls import reverse


def index(request):
    """
    index视图
    :param request: 包含了请求信息的请求对象
    :return: 响应对象
    """
    return HttpResponse("hello the world!")


def haha(request):
    """
    haha视图
    :param request:
    :return:
    """
    _url = reverse('haha:heihei')
    redirect(_url)
    print('这里是函数体, 这里的代码可以随便写')
    return HttpResponse('返回这里的内容到浏览器')


def req(request):
    """
    req test
    :param request:
    :return:
    """
    json_bytes = request.body
    json_str = json_bytes.decode()
    req_data = json.loads(json_str)
    print(req_data)
    return JsonResponse(req_data, content_type="application/json", status=200)

def show_index(request):
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    selected_fruits = sample(fruits, 3)
    return render(request, 'index.html', {'fruits': selected_fruits})