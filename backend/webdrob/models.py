from django.db import models
from django.contrib.auth.models import AbstractUser


# ===========================
#   USUARIO
# ===========================
class User(AbstractUser):
    ROLE_CHOICES = (
        ('usuario', 'Usuario'),
        ('administrador', 'Administrador'),
    )

    PLAN_CHOICES = (
        ('free', 'Free'),
        ('premium', 'Premium'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='usuario')
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES, default='free')

    def _str_(self):
        return self.username


# ===========================
#   PRENDA
# ===========================
class Prenda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prendas')

    categoria = models.CharField(max_length=50)
    color = models.CharField(max_length=50, blank=True, null=True)
    estilo = models.CharField(max_length=50, blank=True, null=True)
    temporada = models.CharField(max_length=50, blank=True, null=True)

    imagen_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.categoria} ({self.color})"


# ===========================
#   ETIQUETA
# ===========================
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ('nombre', 'tipo')

    def _str_(self):
        return f"{self.nombre} ({self.tipo})"


# ===========================
#  TABLA INTERMEDIA PRENDA-ETIQUETA
# ===========================
class PrendaEtiqueta(models.Model):
    prenda = models.ForeignKey(Prenda, on_delete=models.CASCADE, related_name='prenda_etiquetas')
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE, related_name='etiqueta_prendas')

    class Meta:
        unique_together = ('prenda', 'etiqueta')


# ===========================
#   LOOK
# ===========================
class Look(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='looks')
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.nombre


# ===========================
#   LOOK ITEMS (n:m)
# ===========================
class LookItem(models.Model):
    look = models.ForeignKey(Look, on_delete=models.CASCADE, related_name='items')
    prenda = models.ForeignKey(Prenda, on_delete=models.CASCADE, related_name='looks')

    class Meta:
        unique_together = ('look', 'prenda')


# ===========================
#   CALENDARIO
# ===========================
class CalendarioEvento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventos')
    fecha = models.DateField()
    look = models.ForeignKey(Look, on_delete=models.SET_NULL, null=True, blank=True, related_name='eventos')
    notas = models.CharField(max_length=255, blank=True, null=True)

    def _str_(self):
        return f"{self.usuario} - {self.fecha}"


# ===========================
#   RECOMENDACIONES
# ===========================
class Recomendacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recomendaciones')
    look = models.ForeignKey(Look, on_delete=models.CASCADE, related_name='recomendaciones')
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    fecha = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.usuario} → {self.look} ({self.score})"


# ===========================
#   COMENTARIOS
# ===========================
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    look = models.ForeignKey(Look, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Comentario de {self.usuario} en {self.look}"


# ===========================
#   VOTOS
# ===========================
class Voto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votos')
    look = models.ForeignKey(Look, on_delete=models.CASCADE, related_name='votos')
    valor = models.SmallIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'look')

    def _str_(self):
        return f"Voto {self.valor} de {self.usuario} a {self.look}"
