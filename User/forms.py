from django import forms


class CreateUserForm(forms.Form):
    username = forms.CharField(label='username',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'UserName'
                                                             }))
    email = forms.EmailField(label='email',
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Email'}))
    password = forms.IntegerField(label="password",
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
