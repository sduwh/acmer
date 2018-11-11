from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import School, User
from .forms import CreateUserForm


# Create your views here.


@login_required
def user(request):
    """
    返回用户个人中心页面
    :param request: django request
    :return: html
    """
    return render(request, 'user.html')


@login_required
def user_logout(request):
    """
    用户注销
    :param request: django request
    :return:  html
    """
    logout(request)
    return redirect('index')


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
            context = {
                'msg': '',
                'next': request.GET.get('next')
            }
            return render(request, 'login.html', context=context)
        elif request.method == "POST":
            # 获取跳转链接，登录完成返回上一页
            next = request.POST.get('next')
            username = request.POST.get('username')
            password = request.POST.get('password')
            # 如果账号与密码匹配，登录成功，否则返回error messages
            if authenticate(username=username, password=password):
                user = User.objects.filter(username=username).first()
                # 使用自定义的验证 backends
                login(request, user, backend='User.backends.UsernameBackends')
                if next == "None":
                    return redirect('index')
                return redirect(next)

            else:
                context = {
                    'msg': '用户不存在或密码错误'
                }
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
                    user = User.objects.create_user(
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
                    user.school = School.objects.filter(school_name=school).first()
                    user.save()
                    return redirect('user_login')
        else:
            context = {
                'msg': '',
                'form': user_form
            }
            return render(request, 'register.html', context=context)
    else:
        return render(request, 'index.html')
