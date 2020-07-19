#mixins
from post.models import Post
from post.serializer import PostSerializer

from rest_framework import generics 
from rest_framework import mixins

class PostList(mixins.ListModelMixin, mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Post.objects.all() #쿼리셋 등록
    serializer_class = PostSerializer #serializer class 등록
    
    #list 메소드 내보내는 메소드
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    #create 내보내는 메소드
    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
