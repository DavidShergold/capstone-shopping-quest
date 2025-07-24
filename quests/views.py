from django.shortcuts import render
from .models import QuestLog

def quest_log(request):
    if request.user.is_authenticated:
        items = QuestLog.objects.filter(adventurer=request.user)
    else:
        items = []
    return render(request, 'quests/quest_log.html', {'items': items})