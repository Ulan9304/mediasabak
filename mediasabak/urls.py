"""mediasabak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static

from app_views.views import AboutListView, LessonPageListView, LessonDetailView
from mediasabak import settings

urlpatterns = [
    url(r'^$', include('app_views.urls')),
    url(r'^accounts/', include('allauth.urls'),name='auth'),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^about/', AboutListView.as_view(), name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^lessons-page/', LessonPageListView.as_view(), name='category-page'),
    url(r'^details/(?P<pk>\d+)/$', LessonDetailView.as_view(),name='details'),

    # url(r'^app_views/', include('app_views.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
