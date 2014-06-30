from django import forms

class Contacto(forms.Form):
	Email = forms.EmailField(widget=forms.TextInput())
	Titulo = forms.CharField(widget=forms.TextInput())
	Texto = forms.CharField(widget=forms.Textarea())
	