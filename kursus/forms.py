from django.forms import ModelForm
from django import forms
from .models import Materi

class MateriForm(ModelForm):
    class Meta :
        model = Materi
        fields = [
            'judul',
            'isi',
            'kategori',
            'penulis'
        ]
        # mengubah ukuran kolom input pada create.html
        widgets = {
            'judul' : forms.TextInput(attrs={'size':60}),
            'kategori' : forms.TextInput(attrs={'size':60}),
            'penulis': forms.TextInput(attrs={'size':60})
        }