from django.urls import path
from . import views

app_name = 'quests'
urlpatterns = [
    path('', views.quest_log, name='quest_log'),
    path('register/', views.register, name='register'),
    path('shop/add/', views.add_shop, name='add_shop'),
    path('shop/<int:shop_id>/', views.shop_quest_log, name='shop_quest_log'),
    path('shop/<int:shop_id>/delete/', views.delete_shop, name='delete_shop'),
    path('shop/<int:shop_id>/add-objective/', views.add_objective, name='add_objective'),
    path('shop/<int:shop_id>/complete/', views.complete_quest, name='complete_quest'),
    path('shop/<int:shop_id>/reset-bonus/', views.reset_completion_bonus, name='reset_completion_bonus'),  # Debug endpoint
    path('objective/<int:objective_id>/toggle/', views.toggle_objective, name='toggle_objective'),
    path('objective/<int:objective_id>/delete/', views.delete_objective, name='delete_objective'),
]