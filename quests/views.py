from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse
from .models import QuestLog, Shop, QuestObjective
from .forms import ShopForm, QuestLogForm, QuestObjectiveForm, CustomUserCreationForm

def home(request):
    return render(request, 'quests/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in automatically after registration
            login(request, user)
            messages.success(request, f'Welcome to Shopping Quest, {user.username}! Your adventure begins now!')
            return redirect('quests:quest_log')
    else:
        form = CustomUserCreationForm()
    return render(request, 'quests/register.html', {'form': form})

def quest_log(request):
    if request.user.is_authenticated:
        items = QuestLog.objects.filter(adventurer=request.user)
        shops = Shop.objects.filter(adventurer=request.user)
        profile = request.user.userprofile
    else:
        items = []
        shops = []
        profile = None
    return render(request, 'quests/quest_log_new.html', {
        'items': items, 
        'shops': shops,
        'profile': profile
    })

def shop_quest_log(request, shop_id):
    if request.user.is_authenticated:
        shop = get_object_or_404(Shop, id=shop_id, adventurer=request.user)
        items = QuestLog.objects.filter(adventurer=request.user, shop=shop)
        objectives = QuestObjective.objects.filter(adventurer=request.user, shop=shop)
        shops = Shop.objects.filter(adventurer=request.user)
        profile = request.user.userprofile
        
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
        'profile': profile,
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
        was_completed = objective.is_completed
        objective.is_completed = not objective.is_completed
        objective.save()
        
        levels_gained = 0
        completion_bonus = 0
        
        # Award experience for completing objective
        if objective.is_completed and not was_completed:
            levels_gained += objective.award_experience()
        
        # Check for shop completion bonus
        shop_levels = objective.shop.check_completion_bonus()
        levels_gained += shop_levels
        if shop_levels > 0:
            completion_bonus = 30
        
        # Get updated profile info
        profile = request.user.userprofile
        
        return JsonResponse({
            'success': True, 
            'completed': objective.is_completed,
            'levels_gained': levels_gained,
            'completion_bonus': completion_bonus,
            'current_level': profile.level,
            'current_experience': profile.experience,
            'experience_to_next': profile.experience_to_next_level,
            'level_progress': profile.current_level_progress
        })
    return JsonResponse({'success': False})

@login_required
def delete_objective(request, objective_id):
    objective = get_object_or_404(QuestObjective, id=objective_id, adventurer=request.user)
    shop_id = objective.shop.id
    
    if request.method == 'POST':
        objective.delete()
        return redirect('quests:shop_quest_log', shop_id=shop_id)
    
    return render(request, 'quests/delete_objective.html', {'objective': objective})