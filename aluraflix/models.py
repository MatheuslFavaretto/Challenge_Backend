from django.db import models

class Categoria(models.Model):
    titulo = models.CharField(max_length=100)
    cor = models.CharField(max_length=10)

    def __str__(self):
        return self.titulo

class Video(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_DEFAULT, default=1)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    url = models.URLField()

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.categoria_id:
            categoria_livre, _ = Categoria.objects.get_or_create(id=1, titulo='LIVRE', cor='')
            self.categoria = categoria_livre

        super().save(*args, **kwargs)
