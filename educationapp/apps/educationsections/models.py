from django.db import models
import datetime

class Section(models.Model):
    section_name = models.CharField('Название раздела', max_length=50)
    def __str__(self):
        return self.section_name

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

class Content(models.Model):
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField('название', max_length = 200)
    url = models.CharField('ссылка', max_length = 200)
    author = models.CharField('автор', max_length = 200)
    description = models.TextField('описание')
    pub_date = models.DateField('дата публикации')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Сущность"
        verbose_name_plural = "Сущности"