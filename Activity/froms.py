from django import forms


class CreateTeamForm(forms.Form):
    # 队名
    teamName = forms.CharField(label='teamName',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'TeamName'
                                                             }))
    # 队长信息
    inputName1 = forms.CharField(label='inputName1',
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Name'
                                                               }))
    inputEmail1 = forms.EmailField(label='inputEmail1',
                                   widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Email'})
                                   )
    inputPhone1 = forms.IntegerField(label="inputPhone1",
                                     widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'Phone'}))
    inputMajor1 = forms.CharField(label="inputMajor1",
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Major'}))
    inputID1 = forms.IntegerField(label="inputID1",
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'ID'}))
    # 组员1信息
    inputName2 = forms.CharField(label='inputName2',
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Name'}),
                                 required=False)
    inputEmail2 = forms.EmailField(label='inputEmail2',
                                   widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Email'}),
                                   required=False)
    inputPhone2 = forms.IntegerField(label="inputPhone2",
                                     widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'Phone'}),
                                     required=False)
    inputMajor2 = forms.CharField(label="inputMajor2",
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Major'}),
                                  required=False)
    inputID2 = forms.IntegerField(label="inputID2",
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'ID'}),
                                  required=False)
    # 组员2信息
    inputName3 = forms.CharField(label='inputName3',
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Name'}),
                                 required=False)
    inputEmail3 = forms.EmailField(label='inputEmail3',
                                   widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Email'}),
                                   required=False)
    inputPhone3 = forms.IntegerField(label="inputPhone3",
                                     widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'Phone'}),
                                     required=False)
    inputMajor3 = forms.CharField(label="inputMajor3",
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Major'}),
                                  required=False)
    inputID3 = forms.IntegerField(label="inputID3",
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'ID'}),
                                  required=False)

    School = forms.CharField(label="School",
                             widget=forms.Select(attrs={'class': 'form-control',
                                                        'placeholder': 'School'}, ))


class CreatePersonForm(forms.Form):
    inputName = forms.CharField(label='inputName',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Name'
                                                              }))
    inputEmail = forms.EmailField(label='inputEmail',
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Email'}))
    inputPhone = forms.IntegerField(label="inputPhone",
                                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Phone'}))
    inputMajor = forms.CharField(label="inputMajor",
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Major'}))
    inputID = forms.IntegerField(label="inputID",
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'ID'}))

    School = forms.CharField(label="School",
                             widget=forms.Select(attrs={'class': 'form-control',
                                                        'placeholder': 'School'}, ))
