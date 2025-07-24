from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import QuestLog
from .forms import ShopForm, QuestLogForm

def home(request):
    return render(request, 'quests/home.html')

def quest_log(request):
    if request.user.is_authenticated:
        items = QuestLog.objects.filter(adventurer=request.user)
    else:
        items = []
    return render(request, 'quests/quest_log_new.html', {'items': items})

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