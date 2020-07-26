from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from api.views import *


urlpatterns = [
    path('categories/',  CategoryListView.as_view()),
    path('level/',  LevelListView.as_view()),
    path('theme/',  ThemeListView.as_view()),
    path('theme/<int:pk>', ThemeDetailView.as_view()),
    path('word/<int:pk>',  WordDetailView.as_view()),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
