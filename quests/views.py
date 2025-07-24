from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import QuestLog, Shop
from .forms import ShopForm, QuestLogForm

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
        shops = Shop.objects.filter(adventurer=request.user)
    else:
        return redirect('login')
    return render(request, 'quests/quest_log_new.html', {
        'items': items, 
        'shops': shops, 
        'selected_shop': shop
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