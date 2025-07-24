from django.urls import path
from . import views

app_name = 'quests'
urlpatterns = [
    path('', views.quest_log, name='quest_log'),
    path('shop/add/', views.add_shop, name='add_shop'),
    path('shop/<int:shop_id>/', views.shop_quest_log, name='shop_quest_log'),
    path('shop/<int:shop_id>/delete/', views.delete_shop, name='delete_shop'),
    path('shop/<int:shop_id>/add-objective/', views.add_objective, name='add_objective'),
    path('objective/<int:objective_id>/toggle/', views.toggle_objective, name='toggle_objective'),
    path('objective/<int:objective_id>/delete/', views.delete_objective, name='delete_objective'),
]