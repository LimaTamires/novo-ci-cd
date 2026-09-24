from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_destinos, name='catalogo_destinos'),
    path('destino/<int:destino_id>/', views.detalhes_destino, name='detalhes_destino'),
    # Nova rota para a página de orçamento:
    path('destino/<int:destino_id>/orcamento/', views.solicitar_orcamento, name='solicitar_orcamento'),
]