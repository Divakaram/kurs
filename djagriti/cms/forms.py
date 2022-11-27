from django import forms
from cms.models import *


class TeacherForm(forms.ModelForm):
    class Meta:
        model = CmsTeachers
        fields = {"photo", "name", "slug", "napr", "description"}
        widgets = {
            "photo": forms.FileInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Имя'}),
            "slug": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Слаг'}),
            "napr": forms.Select(attrs={"class": "form-select"}),
            "description": forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Описание'})
        }
