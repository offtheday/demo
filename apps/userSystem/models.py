# models.py

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import uuid


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=self.normalize_user(username),
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username=self.normalize_user(username),
            email=self.normalize_email(email),
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    userid = models.UUIDField(
        verbose_name='user id',
        default=uuid.uuid4,
        primary_key=True,
        auto_created=True,
        unique=True,
    )
    avatar = models.ImageField(
        verbose_name='avatar',
        upload_to = "templates/IMAGE/avatar/%Y/%m/%d/",
        #default = "templates/IMAGE/avatar/defaule.JPG",
        blank =True,
        null=True,
    )
    username = models.CharField(
        verbose_name='username',
        max_length=30,
        unique=True,
        blank =True,
        null=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    role_choice = (
        ('0','Administrator'),
        ('1','Normal'),
    )
    role = models.CharField(
        verbose_name= 'role',
        max_length=30,
        default='Normal',
        choices=role_choice,
    )
    gender_choice = (
        ('1','Male'),
        ('2','Female'),
    )
    gender = models.CharField(
        verbose_name='gender', 
        max_length=3,
        choices=gender_choice,  
        default='Male',
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    remember = models.BooleanField(default=False)
    
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin