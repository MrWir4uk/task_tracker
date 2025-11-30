from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('Новий', 'Новий'),
        ('В процесі', 'В процесі'),
        ('Завершено', 'Завершено'),
    ]
    PRIORITY_CHOICES = [
        ('Низький', 'Низький'), 
        ('Середній', 'Середній'), 
        ('Високий', 'Високий'),
    ]
    title = models.CharField(max_length=200, verbose_name='Назва завдання')
    description = models.TextField(verbose_name='Опис завдання', blank=True, null=True)
    deadline = models.DateTimeField(verbose_name='Крайній термін', blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='Новий' ,verbose_name='Статус завдання')
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=50, default='Низький' ,verbose_name='Пріоритет завдання')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    createde_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    

class Coment(models.Model):
    content = models.TextField(verbose_name='Коментар')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    media = models.FileField(upload_to='comments_media/', blank=True, null=True, verbose_name='Медіа файли')
    createde_at = models.DateTimeField(auto_now_add=True)


