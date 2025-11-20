from django.contrib import admin
from .models import (
    User, Prenda, Etiqueta, PrendaEtiqueta,
    Look, LookItem, CalendarioEvento,
    Recomendacion, Comentario, Voto
)

admin.site.register(User)
admin.site.register(Prenda)
admin.site.register(Etiqueta)
admin.site.register(PrendaEtiqueta)
admin.site.register(Look)
admin.site.register(LookItem)
admin.site.register(CalendarioEvento)
admin.site.register(Recomendacion)
admin.site.register(Comentario)
admin.site.register(Voto)
