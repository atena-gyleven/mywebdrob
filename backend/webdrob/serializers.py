from rest_framework import serializers
from .models import (
    User, Prenda, Etiqueta, PrendaEtiqueta,
    Look, LookItem, CalendarioEvento, Recomendacion,
    Comentario, Voto
)


# ===========================
#   USER SERIALIZER
# ===========================
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'role', 'plan'
        ]

# ===========================
#   REGISTER SERIALIZER
# ===========================
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'password',
            'first_name', 'last_name'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)   # muy importante para que la guarde hasheada
        user.save()
        return user


# ===========================
#   ETIQUETA SERIALIZER
# ===========================
class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = '__all__'


# ===========================
#   PRENDA SERIALIZER
# ===========================
class PrendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prenda
        fields = [
            'id', 'usuario', 'categoria', 'color',
            'estilo', 'temporada', 'imagen_url', 'created_at'
        ]
        read_only_fields = ['usuario', 'created_at']


# ===========================
#   LOOK ITEM SERIALIZER
# ===========================
class LookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LookItem
        fields = ['id', 'look', 'prenda']


# ===========================
#   LOOK SERIALIZER
# ===========================
class LookSerializer(serializers.ModelSerializer):
    items = LookItemSerializer(many=True, read_only=True)

    class Meta:
        model = Look
        fields = [
            'id', 'usuario', 'nombre',
            'descripcion', 'created_at', 'items'
        ]
        read_only_fields = ['usuario', 'created_at']


# ===========================
#   CALENDARIO SERIALIZER
# ===========================
class CalendarioEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarioEvento
        fields = '__all__'
        read_only_fields = ['usuario']


# ===========================
#   RECOMENDACION SERIALIZER
# ===========================
class RecomendacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendacion
        fields = '__all__'
        read_only_fields = ['usuario', 'fecha']


# ===========================
#   COMENTARIO SERIALIZER
# ===========================
class ComentarioSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = Comentario
        fields = [
            'id', 'usuario', 'usuario_nombre',
            'look', 'texto', 'fecha'
        ]
        read_only_fields = ['usuario', 'fecha']


# ===========================
#   VOTO SERIALIZER
# ===========================
class VotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voto
        fields = [
            'id', 'usuario', 'look', 'valor', 'fecha'
        ]
        read_only_fields = ['usuario', 'fecha']