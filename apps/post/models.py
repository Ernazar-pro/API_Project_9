from django.db.models import *

class Post(Model):
    title = CharField(verbose_name='Имя поста', max_length=256)
    description = TextField(verbose_name='Описание поста', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'