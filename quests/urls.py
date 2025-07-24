from django.urls import path
from . import views

app_name = 'quests'
urlpatterns = [
    path('', views.quest_log, name='quest_log'),
]