from django.db import models

# Create your models here.
from django.db import models

class Destino(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    foto_principal = models.ImageField(upload_to='destinos/')

    def __str__(self):
        return self.nome

class ImagemAdicional(models.Model):
    destino = models.ForeignKey(Destino, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='destinos/extras/')

class ServicoProduto(models.Model):
    destino = models.ForeignKey(Destino, related_name='servicos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    preco_adicional = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class MensagemContato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    destino_interesse = models.CharField(max_length=200, blank=True)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

class ServicoProduto(models.Model):
    destino = models.ForeignKey(Destino, related_name='servicos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    preco_adicional = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # Linha nova abaixo:
    imagem = models.ImageField(upload_to='servicos/', blank=True, null=True)
    
    def __str__(self):
        return self.nome