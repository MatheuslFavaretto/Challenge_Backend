from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Video, Categoria
from .serializers import VideoSerializer, CategoriaSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CategoriaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as categorias"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET'])
    def videos(self, request, pk=None):
        categoria = self.get_object()
        videos = categoria.video_set.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

class VideoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Videos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]