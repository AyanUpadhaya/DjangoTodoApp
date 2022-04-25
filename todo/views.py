from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
from django.views.generic import UpdateView
from django.urls import reverse,reverse_lazy

# Create your views here.
def home(request):

	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			task = request.POST.get('task')
			Todo.objects.create(item_text= task)
			return redirect('home')
	else:
		form = TodoForm()

	context={'form':form,'title':'Djang Todo','tasks':Todo.objects.all()}
	return render(request,'todo/index.html',context)


def delete_task(request,id):
	# delete/{{task.id}}
	Todo.objects.get(pk=id).delete()
	return redirect('home')



class UpdateView(UpdateView):
	model = Todo
	fields = ['item_text']
	success_url = reverse_lazy('home')


