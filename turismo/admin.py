# Register your models here.
from django.contrib import admin
from .models import Destino, ImagemAdicional, ServicoProduto, MensagemContato

class ImagemAdicionalInline(admin.TabularInline):
    model = ImagemAdicional
    extra = 1

class ServicoProdutoInline(admin.TabularInline):
    model = ServicoProduto
    extra = 1

@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    inlines = [ImagemAdicionalInline, ServicoProdutoInline]

@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'destino_interesse', 'data_envio', 'lida')
    readonly_fields = ('nome', 'email', 'destino_interesse', 'mensagem', 'data_envio')