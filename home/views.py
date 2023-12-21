from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoCreatForm, TodoUpdateForm
from django.contrib import messages

# Create your views here.


def home(request):
   all = Todo.objects.all()
   return render(request, "home.html", {'todos' : all})


def say_hello(request):
   person = {
      "name": "Abolfazl"
   }
   return render(request, template_name="hello.html", context=person) 

def details(request, todo_id):
   todo = Todo.objects.get(id=todo_id)
   return render(request, 'detail.html', {'todo':todo})

def delete(request, todo_id):
   Todo.objects.get(id=todo_id).delete()
   return redirect("home")

def create(request):

   if request.method == "POST":
      form = TodoCreatForm(request.POST)
      if form.is_valid():
         cd = form.cleaned_data
         Todo.objects.create(title=cd['title'], body=cd['body'], created=cd['created'])
         messages.success(request, "ToDo created successfully", 'success')
         return redirect('home')

   else:
      form = TodoCreatForm()

   return render(request, "create.html", {'form': form})



def update(request, todo_id):
   todo = Todo.objects.get(id=todo_id)
   if request.method == 'POST':
      form = TodoUpdateForm(request.POST, instance=todo)
      if form.is_valid():
         form.save()
         messages.success(request, 'your todo updated successfuly', 'success')
         return redirect('details', todo_id)
   else:
      form = TodoUpdateForm(instance=todo)
   return render(request, 'update.html', {'form':form})
 