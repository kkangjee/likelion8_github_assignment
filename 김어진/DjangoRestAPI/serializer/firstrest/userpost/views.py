from rest_framework.authentication import SessionAuthentication,BasicAuthentication, TokenAuthentication

from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    filter_backends=[SearchFilter]
    search_fields=('title', 'body', )
    #어떤 칼럼을 기반으로 검색을 할 것인지? ->무조건 튜플

    def get_queryset(self):
        qs=super().get_queryset()

        # .filter .exclude
        # qs = qs.filter(author__id = 1)

        #로그인X -> 비어있는 쿼리셋 return
        if self.request.user.is_authenticated:
            #로그인O -> 해당 유저의 글만 필터링
            qs=qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        return 

    def perform_create(self, serializer):
        #author field를 save 할거야
        serializer.save(author=self.request.user)
