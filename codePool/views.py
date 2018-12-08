from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .models import Code


@login_required
def code_pool(request, page=1):
    my_codes = Code.objects.filter(is_share=True).order_by('-create_time').all()
    paginator = Paginator(my_codes, 10)
    try:
        code_list = paginator.page(int(page))
    except PageNotAnInteger:
        code_list = paginator.page(1)
    except EmptyPage:
        code_list = paginator.page(paginator.num_pages)
    context = {
        'code_list': code_list
    }
    return render(request, 'codePoolIndex.html', context=context)


@login_required
def my_code_pool(request, page=1):
    """
    我的码池
    :param request:
    :param page: 当前页数
    :return:
    """
    my_codes = Code.objects.filter(user=request.user).order_by('-create_time').all()
    paginator = Paginator(my_codes, 10)
    try:
        code_list = paginator.page(int(page))
    except PageNotAnInteger:
        code_list = paginator.page(1)
    except EmptyPage:
        code_list = paginator.page(paginator.num_pages)
    context = {
        'code_list': code_list
    }
    return render(request, 'codePool.html', context=context)


def code_detail(request, code_id=1):
    """
    代码详情
    :param request:
    :param code_id:
    :return:
    """
    is_author = True
    _code = Code.objects.filter(id=code_id).first()
    if not _code.is_share:
        if request.user != _code.user:
            return HttpResponse('无权限访问')
    if request.user != _code.user:
        is_author = False
    context = {
        'code': _code,
        'is_author': is_author
    }
    return render(request, 'codeDetail.html', context=context)


@login_required
def create_code(request):
    """
    创建代码记录
    :param request:
    :return:
    """
    if request.method == "POST":
        _user = request.user
        code_body = request.POST.get('code')
        code_title = request.POST.get('title')
        is_share = request.POST.get('isShare', False)
        if is_share == 'on':
            is_share = True
        _code = Code.objects.create(code=code_body, user=_user, title=code_title, is_share=is_share)
        return redirect('code_detail', _code.id)
    return render(request, 'codeCreate.html')


@login_required
def del_code(request, code_id=None):
    """删除代码记录"""
    if request.method == "GET":
        _code = Code.objects.filter(id=code_id).first()
        if request.user != _code.user:
            return HttpResponse('无权限访问')
        _code.delete()
        return redirect('code_pool', 1)
    return HttpResponse('method not allowed')


@login_required
def change_code(request, code_id=1):
    """
    修改代码记录
    :param request:
    :param code_id: code id
    :return:
    """
    _code = Code.objects.filter(id=code_id).first()
    if request.method == "POST":
        if request.user != _code.user:
            return HttpResponse('无权限访问')
        code_body = request.POST.get('code')
        code_title = request.POST.get('title')
        is_share = request.POST.get('isShare', False)
        if is_share == 'on':
            is_share = True
        _code.code = code_body
        _code.title = code_title
        _code.is_share = is_share
        _code.save()
        return redirect('code_detail', code_id)
    elif request.method == 'GET':
        context = {
            'code': _code
        }
        return render(request, 'codeChange.html', context=context)
    return HttpResponse('method not allowed')
