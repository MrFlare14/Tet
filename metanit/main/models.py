from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.TextField(max_length=20, verbose_name='Напишите тему поста')
    text = models.TextField(verbose_name='Напишите сам пост')
    def __str__(self):
        return self.title


class Cm(models.Model):
      title = models.TextField(max_length=20)
      def __str__(self):
            return self.title