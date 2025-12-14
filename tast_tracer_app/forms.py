from django import forms
from .models import Task, Comment # Припустимо, у вас є модель Task

class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)

    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status', 'priority'] # Поля для форми

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})  # Додаємо клас Bootstrap для стилізації

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'media'] # Поля для форми

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})  # Додаємо клас Bootstrap для стилізації

            
        
        # Додаткові налаштування форми, якщо потрібно