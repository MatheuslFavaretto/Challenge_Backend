from rest_framework import viewsets, filters
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from .models import Video, Categoria
from .serializers import VideoSerializer, CategoriaSerializer



class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    @action(detail=True, methods=['GET'])
    def videos(self, request, pk=None):
        categoria = self.get_object()
        videos = categoria.video_set.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
