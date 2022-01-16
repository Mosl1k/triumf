from django.db import models
# Create your models here.


class Task(models.Model):
    title = models.CharField('Назваие', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комментарии'
