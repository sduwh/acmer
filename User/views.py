from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .until import encode_url_data, get_referer_url, user_info_to_dict
from django.conf import settings
from .models import School, User
from .forms import CreateUserForm, UserInfoChange, UserLoginForm
import requests
import json

# Create your views here.

SSO_CLIENTID = settings.SSO_CLIENTID
SSO_CLIENTSECRET = settings.SSO_CLIENTSECRET
SSO_CALLBACK = settings.SSO_CALLBACK
SSO_ACCESS_TOKEN = settings.SSO_ACCESS_TOKEN
SSO_AUTHORIZE_URL = settings.SSO_AUTHORIZE_URL
SSO_USER_DATA = settings.SSO_USER_DATA


@login_required
def user(request):
    """
    返回用户个人中心页面
    :param request: django request
    :return: html
    """
    return render(request, 'user.html')


@login_required
def user_info_change(request):
    """
    修改个人信息
    :param request:
    :return:
    """
    if request.method == 'GET':
        schools = [(s.school_name, s.school_name) for s in School.objects.all()]
        _data = user_info_to_dict(request.user)
        user_info_form = UserInfoChange(data=_data)
        user_info_form.fields['school'].widget.choices = schools
        context = {'form': user_info_form}
        return render(request, 'userInfoChange.html', context=context)
    elif request.method == "POST":
        user_info_form = UserInfoChange(request.POST)
        schools = [(s.school_name, s.school_name) for s in School.objects.all()]
        user_info_form.fields['school'].widget.choices = schools
        if user_info_form.is_valid():
            _user = request.user
            _user.real_name = user_info_form.cleaned_data['real_name']
            _user.email = user_info_form.cleaned_data['email']
            _user.student_id = user_info_form.cleaned_data['student_id']
            _user.major = user_info_form.cleaned_data['major']
            _user.grade = user_info_form.cleaned_data['grade']
            _user.school = School.objects.filter(school_name=user_info_form.cleaned_data['school']).first()
            _user.save()
            return redirect('user_center')
        else:
            context = {'form': user_info_form}
            return render(request, 'userInfoChange.html', context=context)
    return render(request, 'user.html')


def sso_login(request):
    """
    第一步: 请求sso第三方登录
    :param request: django request
    :return: 跳转
    """
    data = {
        'client_id': SSO_CLIENTID,
        'client_secret': SSO_CLIENTSECRET,
        'redirect_uri': SSO_CALLBACK,
        'state': get_referer_url(request=request),
    }

    sso_auth_url = '%s?%s' % (SSO_AUTHORIZE_URL, encode_url_data(data))
    return HttpResponseRedirect(sso_auth_url)


def sso_auth(request):
    """
    第二步 sso 认证处理
    :param request:
    :return:
    """
    template_html = 'login.html'
    # 如果申请登陆页面成功后，就会返回code和state
    if 'code' not in request.GET:
        return render(request, template_html)

    code = request.GET.get('code')
    # 将得到的code，通过下面的url请求得到access_token
    access_token_url = SSO_ACCESS_TOKEN
    data = {
        'grant_type': 'authorization_code',
        'client_id': SSO_CLIENTID,
        'client_secret': SSO_CLIENTSECRET,
        'code': code,
        'redirect_uri': SSO_CALLBACK,
    }

    # 设置请求返回的数据类型
    headers = {'Accept': 'application/json'}
    response = requests.get(access_token_url, data=data, headers=headers)
    result = json.loads(response.content)
    # 获取access_token
    access_token = result['access_token']
    url = SSO_USER_DATA + access_token
    response = requests.get(url)
    # 获取用户数据
    data = json.loads(response.content)
    username = data['name']
    password = '111111'
    email = 'acm@acm.com'

    # 如果不存在username，则创建
    if User.objects.filter(username=username).count() == 0:
        User.objects.create_user(username=username,
                                 password=password,
                                 email=email).save()

    # 登陆认证
    sso_user = authenticate(username=username,
                            password=password)
    login(request, sso_user)
    response = HttpResponseRedirect(request.GET['state'])
    response.set_cookie('token', access_token)
    return response


def user_logout(request):
    """
    用户注销
    :param request: django request
    :return:  html
    """
    logout(request)
    response = redirect('index')
    response.delete_cookie('token')
    return response


def user_login(request):
    """
    用户登录
    :param request: django request
    :return: html
    """
    # 判断用户是否已经登录，是则返回，否则继续
    if request.user.is_authenticated:
        return redirect('index')
    else:
        # 限制登录为POST请求，若为GET,返回登录界面
        if request.method == "GET":
            user_login_form = UserLoginForm()
            context = {
                'form': user_login_form,
                'msg': '',
                'next': request.GET.get('next')
            }
            return render(request, 'login.html', context=context)
        elif request.method == "POST":
            # 获取跳转链接，登录完成返回上一页
            _next = request.POST.get('next')
            username = request.POST.get('username')
            password = request.POST.get('password')
            # 如果账号与密码匹配，登录成功，否则返回error messages
            user_login_form = UserLoginForm(request.POST)
            if user_login_form.is_valid():
                if authenticate(username=username, password=password):
                    _user = User.objects.filter(username=username).first()
                    # 使用自定义的验证 backends
                    login(request, _user, backend='User.backends.UsernameBackends')
                    if _next == "None" or _next == '':
                        return redirect('index')
                    return redirect(_next)

                else:
                    context = {'form': user_login_form, 'msg': '用户不存在或密码错误'}
                    return render(request, 'login.html', context=context)
            else:
                context = {'form': user_login_form, 'msg': ''}
                return render(request, 'login.html', context=context)
        else:
            return redirect('index')


def register(request):
    """
    用户注册
    :param request:
    :return:
    """
    # 限制注册为POST请求，若为GET,返回注册界面
    if request.method == "GET":
        # 注册时可选的学校
        schools = [(s.school_name, s.school_name) for s in School.objects.all()]
        user_form = CreateUserForm()
        user_form.fields['school'].widget.choices = schools
        context = {
            'msg': '',
            'form': user_form
        }
        return render(request, 'register.html', context=context)
    elif request.method == "POST":
        # 实例化用户创建的form
        user_form = CreateUserForm(request.POST)
        schools = [(s.school_name, s.school_name) for s in School.objects.all()]
        user_form.fields['school'].widget.choices = schools
        # 如果数据填写合法 继续执行 否则返回error messages
        if user_form.is_valid():
            # 验证用户是否已存在
            if User.objects.filter(username=request.POST.get('username')).count():
                context = {
                    'msg': "该用户名已存在",
                    'form': user_form,
                }
                return render(request, 'register.html', context=context)
            else:
                username = request.POST.get('username')
                email = request.POST.get('email')
                password = request.POST.get('password')
                password1 = request.POST.get('password1')
                # 验证密码是否一致
                if password != password1:
                    context = {
                        'msg': "密码不一致",
                        'form': user_form,
                    }
                    return render(request, 'register.html', context=context)
                school = request.POST.get('school')
                # 验证学校信息是否合法
                if School.objects.filter(school_name=school).count() == 0:
                    context = {
                        'msg': '学校不存在',
                        'form': user_form,
                    }
                    return render(request, 'register.html', context=context)
                real_name = request.POST.get('realName')
                # 创建用户
                try:
                    _user = User.objects.create_user(
                            username=username,
                            email=email,
                            real_name=real_name,
                            password=password,
                        )
                except Exception:
                    context = {
                        'msg': '注册错误',
                        'form': user_form
                    }
                    return render(request, 'register.html', context=context)
                else:
                    _user.school = School.objects.filter(school_name=school).first()
                    _user.save()
                    return redirect('user_login')
        else:
            context = {
                'msg': '',
                'form': user_form
            }
            return render(request, 'register.html', context=context)
    else:
        return render(request, 'index.html')
