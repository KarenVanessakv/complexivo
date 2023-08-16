from django import forms

class FormularioContactanos(forms.Form):
    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()
