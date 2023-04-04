from django import forms
from .models import Task
from  django.db.models import fields




class FormTask(forms.ModelForm):
    tache_name=forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder':'Entrer votre tache',
        'class':'form-control form-control-lg',
    }))
    
    class Meta:
        model=Task
        fields=[
            'tache_name',
        ]
        
    
