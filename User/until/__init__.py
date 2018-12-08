def encode_url_data(data_dict):
    tmp = ''
    for k, v in data_dict.items():
        tmp += '&' + k + '=' + v
    return tmp[1:]


def get_referer_url(request):
    referer_url = request.META.get('HTTP_REFERER')
    if referer_url:
        return referer_url
    return 'http://' + request.META.get('HTTP_HOST')


def user_info_to_dict(obj):
    _school = obj.school
    if not _school:
        _school = 'null'
    _data = {'real_name': obj.real_name, 'email': obj.email, 'school': _school,
             'student_id': obj.student_id, 'major': obj.major, 'grade': obj.grade}
    return _data
