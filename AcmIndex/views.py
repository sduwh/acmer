from django.shortcuts import render


def index(request):
    """
    返回网站首页
    :param request: django request
    :return: html
    """
    return render(request, 'index.html')


