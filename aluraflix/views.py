from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
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
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo']

    @action(detail=False, methods=['GET'])
    def search(self, request):
        search_query = request.GET.get('search')
        if search_query:
            videos = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(videos, many=True)
            return Response(serializer.data)
        else:
            return Response([])

    def perform_create(self, serializer):
        categoria_id = self.request.data.get('categoriaId')
        if not categoria_id:
            try:
                categoria_livre = Categoria.objects.get(id=1)
            except Categoria.DoesNotExist:
                categoria_livre = Categoria.objects.create(id=1, titulo='LIVRE', cor='')

            serializer.validated_data['categoria'] = categoria_livre

        serializer.save()
