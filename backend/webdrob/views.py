from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer

from .models import (
    Prenda, Etiqueta, PrendaEtiqueta,
    Look, LookItem, CalendarioEvento,
    Recomendacion, Comentario, Voto
)
from .serializers import (
    UserSerializer, PrendaSerializer, EtiquetaSerializer,
    LookSerializer, LookItemSerializer, CalendarioEventoSerializer,
    RecomendacionSerializer, ComentarioSerializer, VotoSerializer
)

User = get_user_model()


# ===========================
#   PERMISO BÁSICO (dueño)
# ===========================
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permite leer a cualquiera (GET) pero solo modificar/borrar
    si el objeto pertenece al usuario autenticado.
    Hace que los usuarios no puedan borrar prendas de otros
    """

    def has_object_permission(self, request, view, obj):
        # Lectura: siempre permitida
        if request.method in permissions.SAFE_METHODS:
            return True

        owner = getattr(obj, 'usuario', None)
        return owner == request.user


# ===========================
#   REGISTRO
# ===========================
class RegisterView(APIView):
    """
    POST /api/auth/register/
    Body JSON:
    {
        "username": "andrea",
        "email": "andrea@example.com",
        "password": "tu_clave",
        "first_name": "Andrea",
        "last_name": "Tena"
    }
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ===========================
#   ROL ADMIN
# ===========================
class IsAdmin(permissions.BasePermission):
    """Permite acciones solo a administradores."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'administrador'


# ===========================
#   ROL USER
# ===========================
class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'usuario'

# ===========================
#   USERS (solo lectura)
# ===========================
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


# ===========================
#   PRENDAS
# ===========================
class PrendaViewSet(viewsets.ModelViewSet):
    serializer_class = PrendaSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Evitar errores cuando Swagger genera el esquema (no hay usuario real)
        if getattr(self, 'swagger_fake_view', False):
            return Prenda.objects.none()

        if not self.request or not self.request.user.is_authenticated:
            return Prenda.objects.none()

        return Prenda.objects.filter(usuario=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


# ===========================
#   ETIQUETAS
# ===========================
class EtiquetaViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all().order_by('nombre')
    serializer_class = EtiquetaSerializer
    permission_classes = [permissions.IsAuthenticated]


# ===========================
#   LOOKS
# ===========================
class LookViewSet(viewsets.ModelViewSet):
    serializer_class = LookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Look.objects.none()
        if not self.request or not self.request.user.is_authenticated:
            return Look.objects.none()
        return Look.objects.filter(usuario=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    @action(detail=True, methods=['post'])
    def add_prenda(self, request, pk=None):
        """
        POST /api/looks/<id>/add_prenda/
        Body JSON: { "prenda_id": 3 }
        """
        look = self.get_object()
        prenda_id = request.data.get('prenda_id')

        if not prenda_id:
            return Response({'detail': 'Falta prenda_id'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            prenda = Prenda.objects.get(id=prenda_id, usuario=request.user)
        except Prenda.DoesNotExist:
            return Response({'detail': 'Prenda no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        LookItem.objects.get_or_create(look=look, prenda=prenda)
        return Response({'detail': 'Prenda añadida al look'})


# ===========================
#   CALENDARIO
# ===========================
class CalendarioEventoViewSet(viewsets.ModelViewSet):
    serializer_class = CalendarioEventoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return CalendarioEvento.objects.none()

        if not self.request or not self.request.user.is_authenticated:
            return CalendarioEvento.objects.none()

        return 
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


# ===========================
#   COMENTARIOS
# ===========================
class ComentarioViewSet(viewsets.ModelViewSet):
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Recomendacion.objects.none()

        if not self.request or not self.request.user.is_authenticated:
            return Recomendacion.objects.none()

        return Recomendacion.objects.filter(usuario=self.request.user).order_by('-fecha')

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


# ===========================
#   VOTOS
# ===========================
class VotoViewSet(viewsets.ModelViewSet):
    serializer_class = VotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        look_id = self.request.query_params.get('look')
        qs = Voto.objects.all().order_by('-fecha')
        if look_id:
            qs = qs.filter(look_id=look_id)
        return qs

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


# ===========================
#   RECOMENDACIONES (solo lectura)
# ===========================
class RecomendacionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RecomendacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Recomendacion.objects.filter(usuario=self.request.user).order_by('-fecha')

    @action(detail=False, methods=['get'])
    def simples(self, request):
        """
        Ejemplo de "recomendador simple":
        devuelve los looks con mejores scores.
        """
        looks = Look.objects.all().order_by('-recomendaciones__score')[:10]
        data = LookSerializer(looks, many=True).data
        return Response(data)
