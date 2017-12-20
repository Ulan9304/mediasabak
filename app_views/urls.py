from django.conf.urls import url

from app_views.views import *

urlpatterns = [
    url(r'^$', LessonsListView.as_view(), name='index'),
]