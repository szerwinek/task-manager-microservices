from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_completed', 'user_id', 'created_at')
    list_filter = ('is_completed',)
    search_fields = ('title',)
