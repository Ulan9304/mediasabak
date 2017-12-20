# accounts.models.py
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, UserManager, AbstractUser)


# Create your models here.


class LessonCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    image_field = models.ImageField(verbose_name='icon image')
    item = models.ForeignKey('Lesson',blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория урока'
        verbose_name_plural = 'Категория уроков'


class Lesson(models.Model):
    category = models.ForeignKey(LessonCategory, blank=True, null=True)
    name = models.CharField(verbose_name='Name', max_length=255)
    title = models.CharField(verbose_name='Title', max_length=255)
    text = RichTextUploadingField(verbose_name='Текст урока')
    test  = models.ForeignKey('Test',verbose_name='Выберите тест',blank=True,null=True)
    link = models.CharField(max_length=255, verbose_name='Ссылка на медиа')
    date = models.DateTimeField("Date", auto_now_add=True, null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Потвержденно', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Media(models.Model):
    media_file = models.FileField(verbose_name='Медиа файл')
    link = models.CharField(max_length=255, verbose_name='Ссылка на медиа')
    date = models.DateTimeField("Date", auto_now_add=True, null=True, blank=True)
    lesson = models.ForeignKey(Lesson)

    def __str__(self):
        return self.media_file

    class Meta:
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'


class User(AbstractUser):
    username = models.CharField('Name of user', blank=True, max_length=64, unique=True)
    email = models.EmailField('Email_address', max_length=64, unique=True)
    phone = models.CharField('Phone number', blank=True, null=True, max_length=255)

    # objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_username(self):
        return self.username


class ImageSlide(models.Model):
    name = models.CharField(verbose_name='slide name', max_length=255)
    image = models.ImageField(verbose_name='image')
    date = models.DateTimeField(verbose_name='create date', auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'




class Test(models.Model):
    name = models.CharField(verbose_name='question test', max_length=500)
    image = models.ImageField(verbose_name='picture test')
    correct = models.CharField(verbose_name='right answer message', max_length=500,blank=True)
    incorrect = models.CharField(verbose_name='wrong answer message',max_length=500,blank=True)
    true_answer = models.BooleanField(verbose_name='true test answer')
    false_answer = models.BooleanField(verbose_name='false test anser')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'