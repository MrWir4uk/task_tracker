from django.contrib import admin
from .models import Task, Comment

admin.site.register(Comment)
admin.site.register(Task)

# Register your models here.
