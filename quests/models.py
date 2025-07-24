from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100)
    adventurer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class QuestLog(models.Model):
    name = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    category = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    adventurer = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {'✓' if self.is_completed else ''}"


class QuestObjective(models.Model):
    name = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    adventurer = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['is_completed', '-created_at']

    def __str__(self):
        status = "✓" if self.is_completed else "○"
        qty = f" (x{self.quantity})" if self.quantity > 1 else ""
        return f"{status} {self.name}{qty}"