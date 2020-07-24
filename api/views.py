from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import generics
from api.serializers import *
from .models import *


class CategoryListView(generics.ListAPIView):
    permission_classes = [HasAPIKey]
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()


class LevelListView(generics.ListAPIView):
    serializer_class = LevelDetailSerializer
    queryset = Level.objects.all()

class ThemeListView(generics.ListAPIView):
    serializer_class = ThemeListSerializer
    queryset = Theme.objects.all()

class ThemeDetailView(generics.RetrieveAPIView):
    serializer_class = ThemeDetailSerializer
    queryset = Theme.objects.all()

class WordDetailView(generics.RetrieveAPIView):
    serializer_class = WordDetailSerializer
    queryset = Word.objects.all()

class WordListView(generics.ListAPIView):
    serializer_class = WordListSerializer
    queryset = Word.objects.all()

