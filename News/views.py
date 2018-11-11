from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from News.models import News, NewsPhotos


# Create your views here.


def news(request):
    """
    返回动态中心
    :param request:  django request
    :return: html
    """
    # 获取最新的6条通讯和通知
    message_list = News.objects.filter(news_type='0').order_by('create_time')[:6]
    inform_list = News.objects.filter(news_type='1').order_by('create_time')[:6]
    # 获取三张轮播图
    carousel_list = NewsPhotos.objects.all().order_by('create_time')[:3]
    context = {
        'message_list': message_list,
        'inform_list': inform_list,
        'carousel_list': carousel_list
    }
    return render(request, 'news.html', context=context)


def news_detail(request, news_id):
    """
    获取动态详情
    :param request: django request
    :param news_id: obj New_id
    :return: html
    """
    article = News.objects.filter(id=news_id).first()
    context = {
        'article': article
    }
    return render(request, 'news_detail.html', context=context)


def news_more(request, news_type, page=1):
    """
    更多动态，分类查询
    :param request: django request
    :param news_type: message or inform， new的类别，通讯和通知
    :param page: 当前页
    :return:
    """
    if news_type == 'message':
        context = {
            'title': '通讯',
            'type': news_type
        }
        choice = '0'
    else:
        context = {
            'title': '通知',
            'type': news_type
        }
        choice = '1'
    # 使用django自带的分页包
    articles = News.objects.filter(news_type=choice).order_by('create_time').all()
    # 每14条记录分为一夜
    paginator = Paginator(articles, 14)
    # 获取当前页的内容
    try:
        article_list = paginator.page(int(page))
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)
    context['article_list'] = article_list
    return render(request, 'more.html', context=context)
