from django.urls import include, path
from rest_framework import routers
from aluraflix.views import VideoViewSet, CategoriaViewSet

router = routers.DefaultRouter()
router.register(r'videos', VideoViewSet)
router.register(r'categorias', CategoriaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
