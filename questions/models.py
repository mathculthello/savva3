from django.db import models

# Create your models here.



class Question(models.Model):
    theme = models.CharField(max_length=100,verbose_name="Тема")
    author =  models.CharField(max_length=100, verbose_name="Автор")
    text = models.TextField(verbose_name="Вопрос")

    email = models.EmailField(default="",verbose_name="Электропочта")

    date_added = models.DateTimeField(auto_now_add=True, blank=True)

    published = models.BooleanField(default=False)

    def __str__(self):
        return self.theme
