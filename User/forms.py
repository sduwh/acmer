from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(label='username',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'UserName'
                                                             }))
    password = forms.CharField(label="password",
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'password'}))


class CreateUserForm(forms.Form):
    username = forms.CharField(label='username',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'UserName'
                                                             }))
    email = forms.EmailField(label='email',
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Email'}))
    password = forms.CharField(label="password",
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'password'}))
    password1 = forms.CharField(label="password1",
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'password'}))
    realName = forms.CharField(label="realName",
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Real Name'}))

    school = forms.CharField(label="school",
                             widget=forms.Select(attrs={'class': 'form-control',
                                                        'placeholder': 'school'}, ))


class UserInfoChange(forms.Form):
    real_name = forms.CharField(label="realName",
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': '姓名'}))
    email = forms.EmailField(label='email',
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': '邮箱'}))
    school = forms.CharField(label="school",
                             widget=forms.Select(attrs={'class': 'form-control',
                                                        'placeholder': '学校'}, ))
    student_id = forms.IntegerField(label="studentId",
                                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': '学号'}))
    major = forms.CharField(label='major',
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': '专业'}))
    grade = forms.IntegerField(label="grade",
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': '年级'}))
