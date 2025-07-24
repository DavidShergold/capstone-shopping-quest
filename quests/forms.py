from django import forms
from .models import QuestLog, Shop


class QuestLogForm(forms.ModelForm):
    class Meta:
        model = QuestLog
        fields = ['name', 'category', 'shop']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter quest name...',
                'maxlength': 100
            }),
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category (optional)...',
                'maxlength': 50
            }),
            'shop': forms.Select(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'name': 'Quest Name',
            'category': 'Category',
            'shop': 'Shop (Optional)'
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Filter shops to only show those belonging to the current user
        if user:
            self.fields['shop'].queryset = Shop.objects.filter(adventurer=user)
        else:
            self.fields['shop'].queryset = Shop.objects.none()


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter shop name...',
                'maxlength': 100
            })
        }
        labels = {
            'name': 'Shop Name'
        }


class QuestLogUpdateForm(forms.ModelForm):
    """Form for updating quest completion status"""
    class Meta:
        model = QuestLog
        fields = ['is_completed']
        widgets = {
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        labels = {
            'is_completed': 'Mark as completed'
        }
