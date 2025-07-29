from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=1)
    experience = models.PositiveIntegerField(default=0)
    total_experience = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - Level {self.level} ({self.experience} XP)"

    @property
    def experience_to_next_level(self):
        """Calculate XP needed for next level"""
        return self.get_level_requirement(self.level + 1) - self.total_experience

    @property
    def current_level_progress(self):
        """Calculate progress through current level as percentage"""
        current_level_req = self.get_level_requirement(self.level)
        next_level_req = self.get_level_requirement(self.level + 1)
        level_xp_range = next_level_req - current_level_req
        current_progress = self.total_experience - current_level_req
        return (current_progress / level_xp_range * 100) if level_xp_range > 0 else 100

    @staticmethod
    def get_level_requirement(level):
        """Calculate total XP required for a given level"""
        if level <= 1:
            return 0
        # Level formula: 100 * level^1.5 (gets progressively harder)
        return int(100 * (level ** 1.5))

    def add_experience(self, amount):
        """Add experience and handle level ups"""
        self.experience += amount
        self.total_experience += amount

        # Check for level ups
        new_level = self.calculate_level_from_experience(self.total_experience)
        if new_level > self.level:
            old_level = self.level
            self.level = new_level
            self.save()
            return new_level - old_level  # Return levels gained

        self.save()
        return 0  # No level up

    def calculate_level_from_experience(self, total_xp):
        """Calculate what level player should be based on total XP"""
        level = 1
        while self.get_level_requirement(level + 1) <= total_xp:
            level += 1
        return level


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create UserProfile when User is created"""
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save UserProfile when User is saved"""
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
    else:
        UserProfile.objects.create(user=instance)


class Shop(models.Model):
    name = models.CharField(max_length=100)
    adventurer = models.ForeignKey(User, on_delete=models.CASCADE)
    completion_bonus_awarded = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def check_completion_bonus(self):
        """Check if all objectives are complete and award bonus XP"""
        print(f"DEBUG - check_completion_bonus called for shop: {self.name}")
        objectives = self.questobjective_set.all()
        if objectives.exists() and all(obj.is_completed for obj in objectives):
            if not self.completion_bonus_awarded:
                print(f"DEBUG - Awarding 30 XP bonus for shop: {self.name}")
                profile = self.adventurer.userprofile
                levels_gained = profile.add_experience(30)  # 30 XP bonus for completing all objectives
                self.completion_bonus_awarded = True
                self.save()
                print(f"DEBUG - Bonus awarded, levels gained: {levels_gained}")
                return levels_gained
            else:
                print(f"DEBUG - Bonus already awarded for shop: {self.name}")
        else:
            print(f"DEBUG - Not all objectives complete for shop: {self.name}")
        return 0


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
    experience_awarded = models.BooleanField(default=False)  # Track if XP was given

    class Meta:
        ordering = ['is_completed', '-created_at']

    def __str__(self):
        status = "✓" if self.is_completed else "○"
        qty = f" (x{self.quantity})" if self.quantity > 1 else ""
        return f"{status} {self.name}{qty}"

    def award_experience(self):
        """Award experience for completing this objective"""
        if self.is_completed and not self.experience_awarded:
            profile = self.adventurer.userprofile
            levels_gained = profile.add_experience(10)  # 10 XP per objective
            self.experience_awarded = True
            self.save()
            return levels_gained
        return 0
