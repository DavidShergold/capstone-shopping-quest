from django.contrib import admin
from .models import QuestItem

# Register your models here.

@admin.register(QuestItem)
class QuestItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'is_completed', 'adventurer', 'created_at']
    list_filter = ['is_completed', 'category', 'created_at']
    search_fields = ['name', 'category']
    list_editable = ['is_completed']
