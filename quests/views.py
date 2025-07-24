from django.shortcuts import render
from .models import QuestItem

def quest_log(request):
    if request.user.is_authenticated:
        items = QuestItem.objects.filter(adventurer=request.user)
    else:
        items = []
    return render(request, 'quests/quest_log.html', {'items': items})