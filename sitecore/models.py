# sitecore/models.py
from django.db import models

class PortfolioItem(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='portfolio/')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class PostBlog(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

