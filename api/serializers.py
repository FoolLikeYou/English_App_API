from rest_framework import serializers
from api.models import *



class CategoryDetailSerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LevelDetailSerializer (serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class ThemeListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'

class WordDetailSerializer (serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id','name', 'translation', 'transcription', 'example', 'sound']

class WordListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id','name']

class ThemeDetailSerializer (serializers.ModelSerializer):
    words = WordListSerializer(many=True, read_only=True)

    class Meta:
        model = Theme
        fields = ['id', 'name', 'words']

