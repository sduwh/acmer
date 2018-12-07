from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import datetime


class School(models.Model):
    # 独立学校信息，为日后拓展提供便利
    id = models.AutoField(primary_key=True)
    school_name = models.CharField(
        max_length=256,
        default=""
    )

    def __str__(self):
        return self.school_name
    
    class Meta:
        db_table = "School"
        verbose_name = "学校"
        verbose_name_plural = verbose_name


class UserManager(BaseUserManager):

    def create_user(self, username, password, real_name, email):
        """ 创建，并保存User的username, password, real_name,email"""
        if not username or not password or not email or not real_name:
            raise ValueError('User must have username or password or real_name or email')

        user = self.model(
            username=username,
            real_name=real_name,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, real_name, email):
        """ 创建，并保存SuperUser的username, password, real_name,email"""
        user = self.create_user(username, password, real_name, email)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(
        verbose_name='用户账号',
        max_length=255,
        unique=True
    )
    real_name = models.CharField(max_length=255, null=True, default='')
    email = models.EmailField(
        verbose_name='邮箱地址',
        max_length=255,
        unique=True,)

    student_id = models.IntegerField(
        blank=True,
        null=True
    )
    school = models.ForeignKey(
        'School',
        on_delete=models.DO_NOTHING,
        null=True,
        default=None,
        verbose_name='学校'
    )
    major = models.CharField(max_length=125, default='', blank=True, null=True, verbose_name='专业')
    grade = models.IntegerField(blank=True, null=True, default=datetime.datetime.now().year, verbose_name='年级')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['real_name', 'email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # simplest possible answer: yes
        return True

    def has_module_perms(self, app_label):
        """Does the user have the permission to view the app 'app_label'"""
        # simplest possible answer: yes
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # simplest possible answer: all admins are staff
        return True

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

