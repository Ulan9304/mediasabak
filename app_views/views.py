from django.http import HttpResponse
from django.shortcuts import render
from app_models import models
from django.views.generic import ListView, CreateView, DetailView, TemplateView

# Create your views here.
from app_models.models import Lesson, Media, LessonCategory


class LessonsListView(ListView):
    model = Lesson
    template_name = 'index.html'


class AboutListView(TemplateView):
    template_name = 'about-us.html'


# class MoreListView(TemplateView):
#     template_name = 'more-information.html'


# class BookListView(ListView):
#     template_name = 'books.html'


# class MediaLessonListView():
#     model = Media
#     context_name = 'media_lesson'
#     template_name = 'video_lessons.html'


class LessonPageListView(ListView):
    model = Lesson
    context_object_name = 'all_lessons'
    template_name = 'category-page.html'



# class LessonCategoryListView(ListView):
#     model = LessonCategory
#     context_name = 'lesson_category'
#     template_name = 'category-page.html'


class LessonDetailView(DetailView):
    model = Lesson
    context_object_name = 'lesson'
    template_name = 'lesson-page.html'
