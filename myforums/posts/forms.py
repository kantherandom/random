from django import forms
from .models import posts

class PostForm(forms.ModelForm):
    class Meta:
        CHOICES = (('Financials', 'Financials'),('stockmarket', 'Stock Market'),('Trade', 'Trade'), 
                   ('Politics', 'Politics'), ('videogames', 'Video games'), ('aam', 'Anime and Manga'), 
                   ('Rants', 'Rants'), ('munsic', "Music"), ('Photography', 'Photography'), 
                   ('tech', 'Technology'), ('food', 'Food'), ('offtopic', 'Random'))
        model = posts
        fields = ['author', 'topic', 'content']

        widgets = {
            'content': forms.TextInput(attrs={'class':'form-control'}),
            'topic': forms.Select(choices=CHOICES),
            'author': forms.TextInput(attrs={'class':'form-control' }),
            'image':forms.ImageField
            }