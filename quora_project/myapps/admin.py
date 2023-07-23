from django.contrib import admin
from .models import Question, Answer, Like

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_approved']

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'content', 'is_approved']

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Like)

