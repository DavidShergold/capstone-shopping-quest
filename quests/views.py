from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse
from django.db import models
from .models import QuestLog, Shop, QuestObjective
from .forms import ShopForm, QuestLogForm, QuestObjectiveForm, CustomUserCreationForm, UserProfileForm

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
        # Only show shops where the quest is not yet completed
        shops = Shop.objects.filter(adventurer=request.user, completion_bonus_awarded=False)
        profile = request.user.userprofile
        
        # Add objective information to shops
        shops_with_objectives = []
        for shop in shops:
            objectives = QuestObjective.objects.filter(adventurer=request.user, shop=shop)
            total_objectives = objectives.count()
            completed_objectives = objectives.filter(is_completed=True).count()
            total_items = sum(obj.quantity for obj in objectives)
            completed_items = sum(obj.quantity for obj in objectives.filter(is_completed=True))
            
            shop.objective_count = total_objectives
            shop.completed_objective_count = completed_objectives
            shop.total_items = total_items
            shop.completed_items = completed_items
            shop.progress_percent = (completed_objectives / total_objectives * 100) if total_objectives > 0 else 0
            shops_with_objectives.append(shop)
    else:
        items = []
        shops = []
        shops_with_objectives = []
        profile = None
    return render(request, 'quests/quest_log_new.html', {
        'items': items, 
        'shops': shops,
        'shops_with_objectives': shops_with_objectives,
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
        
        # Check if quest can be completed
        can_complete_quest = total_objectives > 0 and completed_objectives == total_objectives and not shop.completion_bonus_awarded
        
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
        'can_complete_quest': can_complete_quest,
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
        
        # Note: Shop completion bonus is now only awarded via the Complete Quest button
        # No automatic bonus here - must use the button for ceremony!
        
        # Get updated profile info
        profile = request.user.userprofile
        
        # Calculate updated progress for the shop
        shop = objective.shop
        all_objectives = QuestObjective.objects.filter(adventurer=request.user, shop=shop)
        total_objectives = all_objectives.count()
        completed_objectives = all_objectives.filter(is_completed=True).count()
        progress_percentage = (completed_objectives / total_objectives * 100) if total_objectives > 0 else 0
        can_complete_quest = total_objectives > 0 and completed_objectives == total_objectives and not shop.completion_bonus_awarded
        
        return JsonResponse({
            'success': True, 
            'completed': objective.is_completed,
            'levels_gained': levels_gained,
            'completion_bonus': 0,  # No automatic bonus - use Complete Quest button!
            'current_level': profile.level,
            'current_experience': profile.experience,
            'experience_to_next': profile.experience_to_next_level,
            'level_progress': profile.current_level_progress,
            'progress_info': {
                'total_objectives': total_objectives,
                'completed_objectives': completed_objectives,
                'progress_percentage': progress_percentage,
                'can_complete_quest': can_complete_quest
            }
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

@login_required
def complete_quest(request, shop_id):
    """Complete a quest (shop) and award bonus XP"""
    print(f"DEBUG - complete_quest called with shop_id: {shop_id}")
    print(f"DEBUG - request method: {request.method}")
    print(f"DEBUG - is AJAX: {request.headers.get('X-Requested-With') == 'XMLHttpRequest'}")
    
    shop = get_object_or_404(Shop, id=shop_id, adventurer=request.user)
    print(f"DEBUG - shop found: {shop.name}")
    
    # Check if all objectives are completed
    objectives = QuestObjective.objects.filter(shop=shop, adventurer=request.user)
    if not objectives.exists():
        print("DEBUG - no objectives found")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': 'No objectives found for this quest!'})
        messages.error(request, "No objectives found for this quest!")
        return redirect('quests:shop_quest_log', shop_id=shop_id)
    
    all_complete = all(obj.is_completed for obj in objectives)
    print(f"DEBUG - all objectives complete: {all_complete}")
    if not all_complete:
        print("DEBUG - not all objectives complete")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': 'Complete all objectives before finishing the quest!'})
        messages.error(request, "Complete all objectives before finishing the quest!")
        return redirect('quests:shop_quest_log', shop_id=shop_id)
    
    # Check if bonus was already awarded
    print(f"DEBUG - completion bonus already awarded: {shop.completion_bonus_awarded}")
    if shop.completion_bonus_awarded:
        print("DEBUG - bonus already awarded")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': 'Quest completion bonus has already been awarded!'})
        messages.error(request, "Quest completion bonus has already been awarded!")
        return redirect('quests:shop_quest_log', shop_id=shop_id)
    
    # Award completion bonus
    print("DEBUG - about to award completion bonus")
    levels_gained = shop.check_completion_bonus()
    
    # Calculate quest completion stats
    total_objectives = objectives.count()
    total_items = sum(obj.quantity for obj in objectives)
    base_xp = total_objectives * 10  # 10 XP per objective
    bonus_xp = 30  # Quest completion bonus
    total_xp = base_xp + bonus_xp
    
    # Prepare context for congratulations
    context = {
        'shop': shop,
        'total_objectives': total_objectives,
        'total_items': total_items,
        'base_xp': base_xp,
        'bonus_xp': bonus_xp,
        'total_xp': total_xp,
        'levels_gained': levels_gained,
        'user_profile': request.user.userprofile,
    }
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # AJAX request - return JSON for modal
        profile = request.user.userprofile
        return JsonResponse({
            'success': True,
            'shop_name': shop.name,
            'total_objectives': total_objectives,
            'total_items': total_items,
            'base_xp': base_xp,
            'bonus_xp': bonus_xp,
            'total_xp': total_xp,
            'levels_gained': levels_gained,
            'current_level': profile.level,
            'current_experience': profile.experience,
            'experience_to_next': profile.experience_to_next_level,
            'level_progress': profile.current_level_progress,
        })
    else:
        # Regular request - show congratulations page
        return render(request, 'quests/quest_complete.html', context)

@login_required
def edit_shop(request, shop_id):
    """Edit shop name"""
    shop = get_object_or_404(Shop, id=shop_id, adventurer=request.user)
    
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            messages.success(request, f'Shop "{shop.name}" updated successfully!')
            return redirect('quests:quest_log')
    else:
        form = ShopForm(instance=shop)
    
    return render(request, 'quests/edit_shop.html', {'form': form, 'shop': shop})

@login_required
def edit_objective(request, objective_id):
    """Edit objective details"""
    objective = get_object_or_404(QuestObjective, id=objective_id, adventurer=request.user)
    
    if request.method == 'POST':
        form = QuestObjectiveForm(request.POST, instance=objective)
        if form.is_valid():
            form.save()
            messages.success(request, f'Objective "{objective.name}" updated successfully!')
            return redirect('quests:shop_quest_log', shop_id=objective.shop.id)
    else:
        form = QuestObjectiveForm(instance=objective)
    
    return render(request, 'quests/edit_objective.html', {
        'form': form, 
        'objective': objective,
        'shop': objective.shop
    })

@login_required
def edit_profile(request):
    """Edit user profile information"""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('quests:quest_log')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'quests/edit_profile.html', {'form': form})

@login_required
def reset_completion_bonus(request, shop_id):
    """Debug endpoint to reset completion bonus flag"""
    shop = get_object_or_404(Shop, id=shop_id, adventurer=request.user)
    shop.completion_bonus_awarded = False
    shop.save()
    return redirect('quests:shop_quest_log', shop_id=shop_id)

def leaderboard(request):
    """Display leaderboard of top players by level and experience"""
    from .models import UserProfile
    
    # Get top 50 players sorted by level (desc), then by total experience (desc)
    top_players = UserProfile.objects.select_related('user').order_by('-level', '-total_experience')[:50]
    
    # Add ranking
    for i, player in enumerate(top_players):
        player.rank = i + 1
        
    # Get current user's ranking if authenticated
    current_user_rank = None
    current_user_profile = None
    if request.user.is_authenticated:
        try:
            current_user_profile = request.user.userprofile
            # Count how many players are ahead of current user
            players_ahead = UserProfile.objects.filter(
                models.Q(level__gt=current_user_profile.level) |
                models.Q(level=current_user_profile.level, total_experience__gt=current_user_profile.total_experience)
            ).count()
            current_user_rank = players_ahead + 1
        except:
            pass
    
    context = {
        'top_players': top_players,
        'current_user_rank': current_user_rank,
        'current_user_profile': current_user_profile,
        'total_players': UserProfile.objects.count()
    }
    
    return render(request, 'quests/leaderboard.html', context)