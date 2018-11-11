from django.shortcuts import render
from .models import History
# Create your views here.


def join_us(request):
    return render(request, 'join_us.html')


def history(request):
    """
    历程展示, 按照比赛时间优先展示最新的比赛成绩
    :param request: django request
    :return: html
    """
    _history = History.objects.order_by('-create_time').all()
    context = {
        'history_list': _history
    }
    return render(request, 'history.html', context=context)
