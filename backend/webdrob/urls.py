from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    UserViewSet,
    RegisterView,
    PrendaViewSet,
    EtiquetaViewSet,
    LookViewSet,
    CalendarioEventoViewSet,
    ComentarioViewSet,
    VotoViewSet,
    RecomendacionViewSet,
)

router = DefaultRouter()
router.register('usuarios', UserViewSet, basename='usuario')
router.register('prendas', PrendaViewSet, basename='prenda')
router.register('etiquetas', EtiquetaViewSet, basename='etiqueta')
router.register('looks', LookViewSet, basename='look')
router.register('calendario', CalendarioEventoViewSet, basename='calendario')
router.register('comentarios', ComentarioViewSet, basename='comentario')
router.register('votos', VotoViewSet, basename='voto')
router.register('recomendaciones', RecomendacionViewSet, basename='recomendacion')

urlpatterns = [
    # API REST principal
    path('', include(router.urls)),

    # AUTH
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]