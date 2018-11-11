from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from User.models import User, School
# Register your models here.


class UserCreateForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'real_name', 'email', 'is_superuser', 'is_admin')

    def clean_password2(self):
        # 读取表单返回的值
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('PassWord don\'t match')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'real_name', 'is_active', 'is_admin', 'email', 'is_superuser')

    def clean_password(self):
        return self.initial['password']


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm

    list_display = ('username', 'real_name', 'is_admin', 'email', 'is_superuser')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
        ('Personal info', {'fields': ('real_name',)}),
        ('Permissions', {'fields': ('is_admin', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'real_name', 'password1', 'password2', 'email')}
         ),
    )
    search_fields = ('username', 'real_name', 'email')
    ordering = ('username', 'real_name', 'email')
    filter_horizontal = ()


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_name',)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(School, SchoolAdmin)