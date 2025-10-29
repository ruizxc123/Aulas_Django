from django.db import models

# Create your models here.


class Tarefa(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
