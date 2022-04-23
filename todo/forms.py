from django import forms
from .models import Todo
from django.forms import TextInput
class TodoForm(forms.Form):
	task = forms.CharField(label='',widget=forms.TextInput(attrs={'style': 'width: 500px;','class': 'form-control'}),max_length=500)

	class Meta:
		models = Todo
		fields = ['task']
