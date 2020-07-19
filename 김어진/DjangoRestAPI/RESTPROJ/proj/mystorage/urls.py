from rest_framework.routers import DefaultRouter
from django.urls import path, include
from mystorage import views

router = DefaultRouter()
#PostViewSet이라는 뷰셋에 기반에 라우터 등록
router.register('essay', views.PostViewSet, basename='Essay')
router.register('album', views.ImgViewSet)
router.register('files', views.FilePostViewSet)

urlpatterns= [
    path('',include(router.urls))
]