from rest_framework import viewsets
from .models import Essay, Album, Files
from .serializers import EssaySerializer, AlbumSerializer, FileSerializer
from rest_framework.filters import SearchFilter

class PostViewSet(viewsets.ModelViewSet):
    quaryset = Essay.objects.all()
    serializer_class = EssaySerializer(quaryset, many=True)

    filter_backends = [SearchFilter]
    search_fields = ('title','body', )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs=super().get_queryset()
        if self.request.user.is_authenticated:
            qs=qs.filter(author=self.request.user)
        else:
            qs=qs.none()
            
        return qs

class ImgViewSet(viewsets.ModelViewSet):
    quaryset = Album.objects.all()
    serializer_class = AlbumSerializer

from rest_framework.response import Response
from rest_framework import status

class FileViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    
    quaryset = Files.objects.all()
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        serializers = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)

