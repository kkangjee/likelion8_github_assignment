from post.models import Post
from post.serializer import PostSerializer
#status에 따라 직접 Response를 처리할 것
from django.http import Http404 #Get Object or 404 직접 구현
from rest_framework.response import Response 
from rest_framework import status 
#APIView를 상속받은 CBV
from rest_framework.views import APIView
#PostDetail 클래스의 get_object 메소드 대신 써도 됨
#from django.shortcuts import get_object_or_404

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        #쿼리셋 넘기기(many=True인자)
        serializer = PostSerializer(posts, many=True)
        #직접 Response 리턴 해주기 : serializer.data
        return Response(serializer.data)

        def post(self, request):
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid(): #직접 유효성 검사
                serializer.save()     #저장
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#PostList 클래스와는 달리 pk 값을 받음(메소드에 pk 인자)
class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Http404
    
    def get(self, request, pk, format=None):
        post=self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get.objects(pk)
        serializer=PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post=self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)