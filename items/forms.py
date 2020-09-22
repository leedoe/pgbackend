from django import forms
from django.forms import fields
from items.models import Material, Tannery


class TanneryAdminForm(forms.ModelForm):
    imageFile = forms.FileField(required=False)

    class Meta:
        model = Tannery
        fields = '__all__'


class MaterialAdminForm(forms.ModelForm):
    imageFile = forms.FileField(required=False)

    class Meta:
        model = Material
        fields = '__all__'
