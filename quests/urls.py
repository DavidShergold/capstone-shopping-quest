from django.urls import path
from . import views

app_name = 'quests'
urlpatterns = [
    path('', views.quest_log, name='quest_log'),
    path('shop/add/', views.add_shop, name='add_shop'),
    path('shop/<int:shop_id>/', views.shop_quest_log, name='shop_quest_log'),
]