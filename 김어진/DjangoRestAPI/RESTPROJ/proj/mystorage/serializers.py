from .models import Essay
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):
    author_name=serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Essay
        fields =('pk','title','body','author_name')

class AlbumSerializer(serializers.ModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')
    myimage=serializers.ImageField(use_url=True)
    class Meta:
        model = Album
        fields =('pk','author', 'myimage','desc')

class FileSerializer(serializers.ModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')
    myfile=serializers.FileField(use_url=True)
    class Meta:
        model = File
        fields =('pk','author','myfiles','desc')


