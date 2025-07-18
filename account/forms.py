from django import forms
from .models import Profile

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm



class ProfileForm(forms.ModelForm):

    birthday = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        input_formats=['%Y-%m-%d'],
        required=True 
    )

    class Meta:
        model = Profile
        fields = ['photo','birthday', 'category', 'box']


class ProfileFormUpdate(forms.ModelForm):
    

    class Meta: 
        model = Profile
        fields = ['photo']

class CustomCreateUser(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']


    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Usuário já existe')
        return username
    
    def clean_email (self):
        email = self.cleaned_data['email']
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já existe')
        return email
    
    




class UserFormUpdate(UserChangeForm):

    box = forms.ChoiceField(choices=Profile.BOX_CHOICES, required=False)
    category = forms.ChoiceField(choices=Profile.CATEGORY_CHOICES, required=False)
    weight = forms.DecimalField(max_digits= 5, decimal_places = 2, validators=[MaxValueValidator (300), MinValueValidator(0)])
    height = forms.DecimalField(max_digits= 5, decimal_places = 2, validators=[MaxValueValidator (2), MinValueValidator(0)])
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if 'password' in self.fields:
            del self.fields['password']

        
        if self.instance and hasattr(self.instance, 'profile'):
            self.fields['box' ].initial = self.instance.profile.box
            self.fields['category' ].initial = self.instance.profile.category
            self.fields['weight'].initial = self.instance.profile.weight
            self.fields['height'].initial = self.instance.profile.height

    def save(self, commit= True):
        user = super().save(commit = commit)
        box = self.cleaned_data['box']
        category = self.cleaned_data['category']
        weight = self.cleaned_data['weight']
        height = self.cleaned_data['height']
        if commit:
            profile, created = Profile.objects.get_or_create(user=user)
            profile.box = box
            profile.category = category
            profile.weight = weight
            profile.height = height
            profile.save()
        return user



        

