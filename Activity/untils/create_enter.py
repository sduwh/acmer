from Activity.models import Person, Team, Game
from User.models import School


def create_team_enter(data, game_id):
    """
    创建团体活动报名
    :param data: dict 创建的队伍信息
    :param game_id: str 活动id
    :return: dict createInfo
    """
    re = {'status': False}
    school = School.objects.filter(school_name=data['School']).first()
    # 判断学校是否合法
    if school:
        game = Game.objects.filter(id=game_id).first()
        # 检查活动是否合法
        if game:
            # 检查活动下是否存在该队伍， 不存在继续执行 否则返回
            if check_team(data['teamName'], game):
                try:
                    # 创建队伍
                    team = Team.objects.create(
                        team_name=data['teamName'],
                        teacher=' ',
                        game=game
                    )
                except Exception as e:
                    print('![ERROR] %s' % e)
                    re['msg'] = '服务器错误'
                    return re
                # 创建成员
                _re1 = _re2 = _re3 = {'status': True}
                try:
                    _re1 = create_person_of_team(user_name=data['inputName1'],
                                                 email=data['inputEmail1'],
                                                 phone=data['inputPhone1'],
                                                 major=data['inputMajor1'],
                                                 student_id=data['inputID1'],
                                                 school=school,
                                                 team=team,
                                                 is_captain=True,
                                                 game=game)
                    if not _re1['status']:
                        process_error(team)
                        re['msg'] = "成员1已报名"
                        return re
                    if data['inputName2'] != '':
                        _re2 = create_person_of_team(user_name=data['inputName2'],
                                                     email=data['inputEmail2'],
                                                     phone=data['inputPhone2'],
                                                     major=data['inputMajor2'],
                                                     student_id=data['inputID2'],
                                                     school=school,
                                                     team=team,
                                                     game=game)
                        if not _re2['status']:
                            process_error(team)
                            re['msg'] = "成员2已报名"
                            return re
                    if data['inputName3'] != '':
                        _re3 = create_person_of_team(user_name=data['inputName3'],
                                                     email=data['inputEmail3'],
                                                     phone=data['inputPhone3'],
                                                     major=data['inputMajor3'],
                                                     student_id=data['inputID3'],
                                                     school=school,
                                                     team=team,
                                                     game=game)
                        if not _re3['status']:
                            process_error(team)
                            re['msg'] = "成员3已报名"
                            return re

                    re['status'] = True
                    re['msg'] = "报名成功"
                    return re
                except Exception:
                    process_error(team)
                    re['msg'] = '服务器错误'
                    return re
            else:
                re['msg'] = '队伍已存在'
                return re
        else:
            re['msg'] = '活动不存在'
            return re
    else:
        re['msg'] = '学校不存在'
        return re


def create_person_enter(data, game_id):
    """
    创建个人活动报名
    :param data: dict 创建的个人信息
    :param game_id: str 活动id
    :return: dict createInfo
    """
    re = {'status': False}
    school = School.objects.filter(school_name=data['School']).first()
    if school:
        try:
            query_team = Team.objects.filter(team_name=data['inputName'],
                                             teacher=" ",
                                             game=Game.objects.filter(id=game_id).first()).first()
            if query_team is None:
                query_team = Team.objects.create(
                    team_name=data['inputName'],
                    teacher=" ",
                    game=Game.objects.filter(id=game_id).first()
                )

        except Exception as e:
            print("!ERROR % s" % e)
            re['msg'] = '服务器错误'
            return re

        _re = create_person_of_team(user_name=data['inputName'],
                                    email=data['inputEmail'],
                                    phone=data['inputPhone'],
                                    major=data['inputMajor'],
                                    student_id=data['inputID'],
                                    school=school,
                                    team=query_team,
                                    is_captain=True,
                                    game=Game.objects.filter(id=game_id).first())
        if not _re.get('status'):
            re['msg'] = '该人员已报名'
            return re
        else:
            print("*[SUCCESS] create success")
            re['status'] = True
            re['msg'] = '报名成功'
            return re

    else:
        re['msg'] = '学校不存在'
        return re


def check_team(team_name, game):
    """
    检查团队活动的队伍名不可重复
    :param team_name: 队伍名
    :param game:obj 活动对象
    :return: Boolean if not exit return True else return False
    """
    if Team.objects.filter(
            team_name=team_name,
            game=game
    ).first():
        return False
    else:
        return True


def create_person_of_team(user_name, email, phone, major, student_id, school, team, game, is_captain=False):
    """
    创建队伍的成员
    :param user_name: str 姓名
    :param email: str 邮件地址
    :param phone: int 电话号码
    :param major: str 专业
    :param student_id: int 学号
    :param school: obj School对象
    :param team: obj Team对象
    :param is_captain: boolean 是否为对撞
    :param game obj Game对象
    :return: json
    """
    re = {'status': False}
    # 以学号和学校组合识别身份
    if Person.objects.filter(
            student_id=student_id,
            school=school,
            team__game=game
    ).first():
        re['msg'] = "成员已报名"
        return re
    else:
        p = Person.objects.create(user_name=user_name,
                                  email=email,
                                  phone=phone,
                                  major=major,
                                  student_id=student_id,
                                  school=school,
                                  team=team)
        if is_captain:
            p.is_captain = True
        p.save()
        re['status'] = True
        return re


def process_error(team):
    """
    创建成员时出错处理
    :param team: obj Team对象
    :return: None
    """
    persons = Person.objects.filter(team=team).all()
    for pre in persons:
        pre.delete()
    team.delete()
    return
