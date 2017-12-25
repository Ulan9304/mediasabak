from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin

from .models import *
# Register your models here.
class ImagesInline(admin.StackedInline):
    model = ImageSlide
    exta = 2

class MediaInline(admin.StackedInline):
    model = Media
    extra = 2

class LessonAdmin(admin.ModelAdmin):
    inlines = (ImagesInline,)

admin.site.register(Lesson,LessonAdmin)
admin.site.register(LessonCategory)
admin.site.register(Media)
# admin.site.register(ImageSlide)
admin.site.register(Test)