from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import QuestLog, Shop, QuestObjective
from .forms import ShopForm, QuestLogForm, QuestObjectiveForm

def home(request):
    return render(request, 'quests/home.html')

def quest_log(request):
    if request.user.is_authenticated:
        items = QuestLog.objects.filter(adventurer=request.user)
        shops = Shop.objects.filter(adventurer=request.user)
    else:
        items = []
        shops = []
    return render(request, 'quests/quest_log_new.html', {'items': items, 'shops': shops})

def shop_quest_log(request, shop_id):
    if request.user.is_authenticated:
        shop = get_object_or_404(Shop, id=shop_id, adventurer=request.user)
        items = QuestLog.objects.filter(adventurer=request.user, shop=shop)
        objectives = QuestObjective.objects.filter(adventurer=request.user, shop=shop)
        shops = Shop.objects.filter(adventurer=request.user)
        
        # Calculate progress
        total_objectives = objectives.count()
        completed_objectives = objectives.filter(is_completed=True).count()
        progress_percentage = (completed_objectives / total_objectives * 100) if total_objectives > 0 else 0
        
    else:
        return redirect('login')
    return render(request, 'quests/shop_objectives.html', {
        'items': items, 
        'objectives': objectives,
        'shops': shops, 
        'selected_shop': shop,
        'total_objectives': total_objectives,
        'completed_objectives': completed_objectives,
        'progress_percentage': progress_percentage,
    })

@login_required
def add_shop(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.adventurer = request.user
            shop.save()
            return redirect('quests:quest_log')  # Updated to use namespaced URL
    else:
        form = ShopForm()

    return render(request, 'quests/add_shop.html', {'form': form})

@login_required
def delete_shop(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id, adventurer=request.user)
    
    if request.method == 'POST':
        shop_name = shop.name
        shop.delete()
        return redirect('quests:quest_log')
    
    return render(request, 'quests/delete_shop.html', {'shop': shop})

@login_required
def add_objective(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id, adventurer=request.user)
    
    if request.method == 'POST':
        form = QuestObjectiveForm(request.POST)
        if form.is_valid():
            objective = form.save(commit=False)
            objective.shop = shop
            objective.adventurer = request.user
            objective.save()
            return redirect('quests:shop_quest_log', shop_id=shop.id)
    else:
        form = QuestObjectiveForm()
    
    return render(request, 'quests/add_objective.html', {'form': form, 'shop': shop})

@login_required
def toggle_objective(request, objective_id):
    if request.method == 'POST':
        objective = get_object_or_404(QuestObjective, id=objective_id, adventurer=request.user)
        objective.is_completed = not objective.is_completed
        objective.save()
        return JsonResponse({'success': True, 'completed': objective.is_completed})
    return JsonResponse({'success': False})

@login_required
def delete_objective(request, objective_id):
    objective = get_object_or_404(QuestObjective, id=objective_id, adventurer=request.user)
    shop_id = objective.shop.id
    
    if request.method == 'POST':
        objective.delete()
        return redirect('quests:shop_quest_log', shop_id=shop_id)
    
    return render(request, 'quests/delete_objective.html', {'objective': objective})