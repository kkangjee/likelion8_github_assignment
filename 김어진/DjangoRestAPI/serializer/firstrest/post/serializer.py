from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        #fields = ['id','title', 'body']
        read_only_fields=('title', )
        #title을 read_only_filed 즉, 수정이 불가한 항목으로 설정
        

