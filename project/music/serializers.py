from rest_framework import serializers
from .models import *

class SingerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField()
    debut = serializers.DateField()

    songs = serializers.SerializerMethodField(read_only=True)
    tags = serializers.SerializerMethodField(read_only=True)
    image = serializers.ImageField(use_url=True, required=False)

    def get_songs(self, instance):
        serializer = SongSerializer(instance.songs, many=True)
        return serializer.data

    def get_tags(self, instance):
        tags = instance.tags.all()
        return [tag.name for tag in tags]

    class Meta:
        model = Singer
        fields = ['id', 'content', 'debut', 'songs','tags','image']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['singer']

class TagSerializer(serializers.ModelSerializer):
        model = Tag
        fields = '__all__'