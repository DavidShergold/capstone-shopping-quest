from django.contrib import admin
from .models import QuestLog

# Register your models here.

@admin.register(QuestLog)
class QuestLogAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'is_completed', 'adventurer', 'created_at']
    list_filter = ['is_completed', 'category', 'created_at']
    search_fields = ['name', 'category']
    list_editable = ['is_completed']
