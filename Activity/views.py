from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required

from datetime import datetime

from .models import Game
from .froms import CreatePersonForm, CreateTeamForm
from User.models import School as all_school
from Activity.untils.create_enter import create_person_enter, create_team_enter


def activity(request, page=1):
    """
    活动首页
    :param request: django request
    :param page: 页数
    :return: html
    """
    if request.method == 'GET':
        # 使用django自带分页
        games = Game.objects.order_by('-create_time').all()
        paginator = Paginator(games, 14)
        try:
            game_list = paginator.page(int(page))
        except PageNotAnInteger:
            game_list = paginator.page(1)
        except EmptyPage:
            game_list = paginator.page(paginator.num_pages)
        context = {
            'game_list': game_list
        }
        return render(request, 'activity.html', context=context)


@login_required
def activity_detail(request, gid):
    """
    活动详情
    :param request: django request
    :param gid: 活动id，用于查询活动obj
    :return: html
    """
    # 查询所有学校
    schools = [(s.school_name, s.school_name) for s in all_school.objects.all()]
    if request.method == 'GET':
        game = Game.objects.filter(id=gid).first()
        # 如果已经结束报名 直接返回
        if game.end_enter_time < datetime.now():
            return redirect('activity', 1)
        # 更具活动的类别创建不同的form ‘0’=》团体 ‘1’=》个人
        if game.game_type == "0":
            form = CreateTeamForm()
        else:
            form = CreatePersonForm()
        form.fields['School'].widget.choices = schools
        context = {
            'game': game,
            'form': form,
            'msg': ''
        }
        return render(request, 'activity_detail.html', context=context)
    else:
        return redirect('index')


@login_required
def enter(request):
    """
    报名 函数
    :param request: django request
    :return:
    """
    if request.method == 'POST':
        # 查询所有学校
        schools = [(s.school_name, s.school_name) for s in all_school.objects.all()]
        # 获取活动类别 ‘1’=》个 ‘0’=》人团体，并实例化不同的form
        game_type = request.POST.get('game_type')
        if game_type == "0":
            form = CreateTeamForm(request.POST)
        else:
            form = CreatePersonForm(request.POST)
        form.fields['School'].widget.choices = schools
        context = {'form': form, 'msg': ''}
        gid = request.POST.get('game_id')
        # 验证输入的数据合法性，合法继续执行，不合法返回error messages
        if form.is_valid():
            # 根据活动类别，创建数据
            if game_type == "0":
                re = create_team_enter(form.cleaned_data, gid)
            else:
                re = create_person_enter(form.cleaned_data, gid)
            # 如果报名成功，跳转到成功页面，否则返回error messages
            if re.get('status'):
                return redirect('enter_success')
            game = Game.objects.filter(id=gid).first()
            context['game'] = game
            context['msg'] = re.get('msg')
            return render(request, 'activity_detail.html', context=context)
        else:
            game = Game.objects.filter(id=gid).first()
            context['game'] = game
            return render(request, 'activity_detail.html', context=context)
    else:
        return redirect('index')


@login_required
def enter_success(request):
    return render(request, 'activity_enter_success.html')
