from rest_framework import serializers
from .models import Categoria, Video

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'titulo', 'cor']

class VideoSerializer(serializers.ModelSerializer):
    categoriaId = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source='categoria', required=False)

    class Meta:
        model = Video
        fields = ['id', 'categoriaId', 'titulo', 'descricao', 'url']

    def create(self, validated_data):
        categoria_id = validated_data.pop('categoriaId', None)
        if not categoria_id:
            categoria_livre, _ = Categoria.objects.get_or_create(id=1, titulo='LIVRE', cor='')
            validated_data['categoria'] = categoria_livre
        else:
            validated_data['categoria'] = categoria_id
        return super().create(validated_data)