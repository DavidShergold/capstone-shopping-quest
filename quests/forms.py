from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import QuestLog, Shop, QuestObjective


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


class QuestObjectiveForm(forms.ModelForm):
    """Form for adding new quest objectives"""
    class Meta:
        model = QuestObjective
        fields = ['name', 'quantity', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item name...',
                'maxlength': 200
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'value': 1
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Additional notes (optional)...',
                'rows': 3
            })
        }
        labels = {
            'name': 'Item Name',
            'quantity': 'Quantity',
            'notes': 'Notes'
        }


class QuestObjectiveUpdateForm(forms.ModelForm):
    """Form for updating objective completion status"""
    class Meta:
        model = QuestObjective
        fields = ['is_completed']
        widgets = {
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'objective-checkbox'
            })
        }


class CustomUserCreationForm(UserCreationForm):
    """Custom registration form with styled fields"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address...'
        })
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose a username...'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Style the password fields
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Create a password...'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password...'
        })
        
        # Update labels
        self.fields['username'].label = 'Adventurer Name'
        self.fields['email'].label = 'Email Address'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
        
        # Update help texts
        self.fields['username'].help_text = 'Choose a unique name for your shopping adventures!'
        self.fields['password1'].help_text = 'Your password must be at least 8 characters long.'
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
