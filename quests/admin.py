from django.contrib import admin
from .models import QuestLog, Shop, QuestObjective

# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'adventurer']
    list_filter = ['adventurer']
    search_fields = ['name']


@admin.register(QuestLog)
class QuestLogAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'shop', 'is_completed', 'adventurer', 'created_at']
    list_filter = ['is_completed', 'category', 'shop', 'created_at']
    search_fields = ['name', 'category', 'shop__name']
    list_editable = ['is_completed']


@admin.register(QuestObjective)
class QuestObjectiveAdmin(admin.ModelAdmin):
    list_display = ['name', 'shop', 'quantity', 'is_completed', 'adventurer', 'created_at']
    list_filter = ['is_completed', 'shop', 'created_at']
    search_fields = ['name', 'shop__name', 'notes']
    list_editable = ['is_completed']
